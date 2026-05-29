---
type: policy
status: active
owner: knowledge-steward
created: 2026-04-19
updated: 2026-04-19
visibility: company
confidence: high
officiality: reviewed
domain: governance
domains: [governance, naming, discoverability, wiki-structure]
review_cycle: quarterly
verification_status: spot-checked
related:
  - ./metadata-schema.md
  - ./official-surface-policy.md
  - ./write-back-policy.md
  - ../dashboards/official-start-here.md
---

# 命名与可发现性政策

## 目标
提升公司内部的中文可发现性，同时保持路径稳定、链接耐久、脚本友好。

## 默认规则
1. `wiki/` 下的文件名默认保持英文 slug，不为了中文可读性而批量改名。
2. 面向广泛内部阅读的 canonical 页面，`H1` 默认中文优先；首次出现的重要实体可保留英文并列。
3. 重要维护页应补齐：
   - `aliases`
   - `name_zh`
   - `name_en`
4. 中文可发现性优先通过标题、别名、导航页、dashboard 提升，而不是通过频繁重命名路径实现。

## 为什么不默认改中文文件名
- 英文 slug 更稳定，减少链接断裂和重命名成本。
- Git、终端、脚本、跨系统同步对英文路径更友好。
- 标题和别名是给人读和给人搜的；文件名首先服务于结构稳定。

## 标题规则
### canonical 页面
- 推荐：`# 中文名（English Name）`
- 如果英文实体本身就是主要识别名，也可写成：`# 中文名（Amazon JP）`

### 工作流 / playbook
- 推荐：`# 中文名（English Name）`
- 如果内部已经大量以英文称呼，也至少补中文别名。

### source-summary
- 允许继续采用 `来源摘要｜...` 的中文主标题。

## 别名规则
- `aliases` 至少覆盖一种中文检索说法和一种英文检索说法。
- 若存在常见缩写、俗称、旧叫法，也应纳入。
- 不要把无关近义词堆进 `aliases`，以免污染检索。

## 导航规则
- 保持一个明确中文入口页，面向广泛内部阅读。
- 重要主题簇应在 canonical 页中显式列出下一步阅读路径。
- 当某个目录增长过快时，优先补导航页，不优先改路径。
