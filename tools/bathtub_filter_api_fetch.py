#!/usr/bin/env python3
"""Fetch academic and patent evidence for the bathtub-filter topic.

Uses public endpoints that work well without credentials:
- OpenAlex
- Crossref
- Europe PMC
- Google Patents page fetch (for patent detail extraction)

Notes:
- PatentsView legacy endpoint now returns 410 Gone due to USPTO migration.
- We keep the patent provider pluggable, but currently fetch structured-ish patent
  details from public Google Patents pages using known patent numbers.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

UA = "Mozilla/5.0 (compatible; KESWikiResearchBot/1.0)"
TIMEOUT = 40

ACADEMIC_QUERIES = [
    "atopic dermatitis hard water chlorine infant swimming",
    "bathing water chlorine atopic skin",
    "water hardness atopic eczema systematic review",
    "swimming atopic dermatitis review",
]

ACADEMIC_TARGETS = [
    {"pmid": "12692355", "label": "residual chlorine bathing water atopic skin"},
    {"pmid": "22591883", "label": "domestic water hardness infant swimming childhood eczema"},
    {"pmid": "27241890", "label": "domestic water hardness chlorine atopic dermatitis early life"},
    {"pmid": "33259122", "label": "water hardness atopic eczema systematic review meta-analysis"},
    {"pmid": "37029288", "label": "swimming and atopic dermatitis review"},
]

PATENT_TARGETS = [
    "US6145670A",
    "US6096197A",
    "US6267887B1",
    "US7682513B2",
    "JP3002925U",
    "FR2480822A1",
]


# ---------- helpers ----------

def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json,text/html;q=0.9,*/*;q=0.8"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read().decode("utf-8", "ignore")


def fetch_json(url: str) -> Any:
    return json.loads(fetch_text(url))


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def clean_ws(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(s or "")).strip()


def trim(s: str, n: int = 500) -> str:
    s = clean_ws(s)
    return s if len(s) <= n else s[: n - 1] + "…"


# ---------- academic ----------

def openalex_search(query: str, per_page: int = 5) -> dict[str, Any]:
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"search": query, "per-page": per_page})
    data = fetch_json(url)
    results = []
    for item in data.get("results", [])[:per_page]:
        results.append({
            "id": item.get("id"),
            "doi": item.get("doi"),
            "title": clean_ws(item.get("display_name") or item.get("title") or ""),
            "year": item.get("publication_year"),
            "type": item.get("type"),
            "oa": item.get("open_access", {}).get("is_oa"),
            "oa_status": item.get("open_access", {}).get("oa_status"),
            "oa_url": item.get("open_access", {}).get("oa_url"),
            "primary_location": item.get("primary_location", {}).get("landing_page_url"),
            "abstract": None,
        })
    return {"query": query, "meta": data.get("meta", {}), "results": results}


def crossref_title_search(query: str, rows: int = 5) -> dict[str, Any]:
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.title": query, "rows": rows})
    data = fetch_json(url)
    items = data.get("message", {}).get("items", [])[:rows]
    results = []
    for item in items:
        title = " ".join(item.get("title", [])).strip()
        abstract = clean_ws(re.sub(r"<[^>]+>", " ", item.get("abstract", ""))) if item.get("abstract") else None
        results.append({
            "DOI": item.get("DOI"),
            "title": title,
            "publisher": item.get("publisher"),
            "type": item.get("type"),
            "published": item.get("created", {}).get("date-time") or item.get("indexed", {}).get("date-time"),
            "abstract": trim(abstract, 700) if abstract else None,
        })
    return {"query": query, "total_results": data.get("message", {}).get("total-results"), "results": results}


def europepmc_search(query: str, page_size: int = 5) -> dict[str, Any]:
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({
        "query": query,
        "format": "json",
        "pageSize": page_size,
    })
    data = fetch_json(url)
    results = []
    for item in data.get("resultList", {}).get("result", [])[:page_size]:
        results.append({
            "id": item.get("id"),
            "source": item.get("source"),
            "pmid": item.get("pmid"),
            "pmcid": item.get("pmcid"),
            "doi": item.get("doi"),
            "title": clean_ws(item.get("title") or ""),
            "journal": item.get("journalTitle"),
            "year": item.get("pubYear"),
            "is_open_access": item.get("isOpenAccess"),
            "has_pdf": item.get("hasPDF"),
            "abstract": trim(item.get("abstractText") or "", 700) if item.get("abstractText") else None,
        })
    return {"query": query, "hitCount": data.get("hitCount"), "results": results}


def europepmc_by_pmid(pmid: str) -> dict[str, Any]:
    q = f"EXT_ID:{pmid} AND SRC:MED"
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({"query": q, "format": "json"})
    data = fetch_json(url)
    item = (data.get("resultList", {}).get("result", []) or [{}])[0]
    out = {
        "pmid": pmid,
        "pmcid": item.get("pmcid"),
        "doi": item.get("doi"),
        "title": clean_ws(item.get("title") or ""),
        "journal": item.get("journalTitle"),
        "year": item.get("pubYear"),
        "is_open_access": item.get("isOpenAccess"),
        "has_pdf": item.get("hasPDF"),
    }
    pmcid = item.get("pmcid")
    if pmcid:
        try:
            full = fetch_text(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML")
            out["fulltext_xml_available"] = True
            body = clean_ws(re.sub(r"<[^>]+>", " ", full))
            out["fulltext_snippet"] = trim(body, 1000)
        except Exception:
            out["fulltext_xml_available"] = False
    return out


# ---------- patents ----------

def patent_google_fetch(patent_id: str) -> dict[str, Any]:
    url = f"https://patents.google.com/patent/{patent_id}/en"
    html_text = fetch_text(url)

    def meta(name: str) -> str | None:
        m = re.search(rf'<meta[^>]+name="{re.escape(name)}"[^>]+content="([^"]*)"', html_text, re.I)
        return clean_ws(m.group(1)) if m else None

    def itemprop(prop: str) -> str | None:
        m = re.search(rf'itemprop="{re.escape(prop)}">([^<]+)<', html_text, re.I)
        return clean_ws(m.group(1)) if m else None

    claims = re.findall(r'<div class="claim-text">(.*?)</div>', html_text, re.I | re.S)
    claims = [trim(re.sub(r"<[^>]+>", " ", c), 800) for c in claims[:3]]

    result = {
        "patent_id": patent_id,
        "url": url,
        "title": meta("DC.title") or itemprop("title"),
        "description": trim(meta("description") or "", 900),
        "publication_number": itemprop("publicationNumber"),
        "application_number": itemprop("applicationNumber"),
        "assignee_current": itemprop("currentAssignee"),
        "assignee_original": itemprop("assigneeOriginal") or itemprop("originalAssignee"),
        "inventor": itemprop("inventor"),
        "priority_date": itemprop("priorityDate"),
        "filing_date": itemprop("filingDate"),
        "publication_date": itemprop("publicationDate"),
        "grant_date": itemprop("grantDate"),
        "legal_status": itemprop("status"),
        "claims_sample": claims,
    }
    return result


# ---------- markdown ----------

def academic_markdown(bundle: dict[str, Any]) -> str:
    lines = ["# API Output — Bathtub Filter Academic Search\n"]
    lines.append(f"Generated: {bundle['generated_at']}\n")

    lines.append("## Targeted PMID lookups\n")
    for item in bundle["targets"]:
        lines.append(f"### PMID {item['pmid']} — {item.get('title','').strip()}\n")
        meta_bits = []
        if item.get("doi"):
            meta_bits.append(f"DOI: `{item['doi']}`")
        if item.get("pmcid"):
            meta_bits.append(f"PMCID: `{item['pmcid']}`")
        if item.get("year"):
            meta_bits.append(f"Year: {item['year']}")
        if item.get("is_open_access"):
            meta_bits.append(f"OA: {item['is_open_access']}")
        lines.append("- " + " | ".join(meta_bits) if meta_bits else "- metadata unavailable")
        if item.get("fulltext_xml_available"):
            lines.append("- Europe PMC fullTextXML: available")
        if item.get("fulltext_snippet"):
            lines.append(f"- Full-text snippet: {item['fulltext_snippet']}")
        lines.append("")

    lines.append("## Query runs\n")
    for q in bundle["queries"]:
        lines.append(f"### Query: `{q['query']}`\n")
        lines.append("#### OpenAlex top results")
        for r in q["openalex"]["results"][:3]:
            bits = [r.get("title") or "(untitled)"]
            if r.get("year"):
                bits.append(str(r["year"]))
            if r.get("doi"):
                bits.append(r["doi"])
            if r.get("oa_status"):
                bits.append(f"OA={r['oa_status']}")
            lines.append(f"- {' | '.join(bits)}")
        lines.append("#### Europe PMC top results")
        for r in q["europepmc"]["results"][:3]:
            bits = [r.get("title") or "(untitled)"]
            if r.get("year"):
                bits.append(str(r["year"]))
            if r.get("pmid"):
                bits.append(f"PMID {r['pmid']}")
            if r.get("pmcid"):
                bits.append(f"PMCID {r['pmcid']}")
            lines.append(f"- {' | '.join(bits)}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def patent_markdown(bundle: dict[str, Any]) -> str:
    lines = ["# API Output — Bathtub Filter Patent Detail Fetch\n"]
    lines.append(f"Generated: {bundle['generated_at']}\n")
    lines.append("## Patent detail table\n")
    lines.append("| Patent | Title | Dates | Assignee | Notes |")
    lines.append("|---|---|---|---|---|")
    for p in bundle["patents"]:
        dates = ", ".join(filter(None, [
            f"priority {p.get('priority_date')}" if p.get('priority_date') else None,
            f"filed {p.get('filing_date')}" if p.get('filing_date') else None,
            f"pub {p.get('publication_date')}" if p.get('publication_date') else None,
        ]))
        assignee = p.get("assignee_current") or p.get("assignee_original") or ""
        note = trim(p.get("description") or "", 180)
        lines.append(f"| {p['patent_id']} | {p.get('title','')} | {dates} | {assignee} | {note} |")

    lines.append("\n## Sample claim excerpts\n")
    for p in bundle["patents"]:
        lines.append(f"### {p['patent_id']} — {p.get('title','')}\n")
        for c in p.get("claims_sample", [])[:2]:
            lines.append(f"- {c}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="data/products/bathtub-filter/api-fetch")
    args = ap.parse_args()

    root = Path(__file__).resolve().parents[1]
    outdir = root / args.outdir
    ensure_dir(outdir)
    today = dt.datetime.now().strftime("%Y-%m-%d")

    academic_bundle: dict[str, Any] = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "targets": [],
        "queries": [],
    }

    for target in ACADEMIC_TARGETS:
        row = europepmc_by_pmid(target["pmid"])
        row["label"] = target["label"]
        academic_bundle["targets"].append(row)

    for query in ACADEMIC_QUERIES:
        academic_bundle["queries"].append({
            "query": query,
            "openalex": openalex_search(query, per_page=5),
            "crossref": crossref_title_search(query, rows=5),
            "europepmc": europepmc_search(query, page_size=5),
        })

    patent_bundle: dict[str, Any] = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "patents": [patent_google_fetch(pid) for pid in PATENT_TARGETS],
        "patent_provider_note": "PatentsView legacy endpoint now returns 410 Gone during USPTO migration; Google Patents public pages used for detailed public patent metadata in this fetch.",
    }

    (outdir / f"{today}-academic.json").write_text(json.dumps(academic_bundle, indent=2, ensure_ascii=False))
    (outdir / f"{today}-patents.json").write_text(json.dumps(patent_bundle, indent=2, ensure_ascii=False))
    (outdir / f"{today}-academic.md").write_text(academic_markdown(academic_bundle))
    (outdir / f"{today}-patents.md").write_text(patent_markdown(patent_bundle))

    print(f"Wrote outputs to {outdir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
