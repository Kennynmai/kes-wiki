# "AI 接单 → 参数化设计 → 在地加工 → 快速交付" 技术与运营底座调研（Agent 调研原文）

- 日期：2026-09-06
- 方法：约 35 次搜索 + 30 次抓取；Shapeways support、Opendesk Medium、Etsy、Home Depot、Amazon 商品页 403，标 (snippet)
- 性质：一次性侦察记录，未加工

## 1. 现有参数化 / AI 配置器

### Tylko（华沙）— 最接近的参数化 → CNC 案例
- 滑块配置器，"fully automated CNC machines that receive production files directly from customers"；波兰制造；2017 交期 3–6 周；IKEA Billy ~€40 vs Tylko ~€440；2017-03 约 3,000 客户，Series A €3M。https://techcrunch.com/2017/03/07/tylko-bags-3-1m-to-size-up-a-bespoke-furniture-business/
- 累计融资 $52.1M；最新一轮 2023-12 EIB 债务 $8.07M (snippet)；2020 营收 €36M（+132%）；2022 €60M (snippet)；员工 ~199，-9% (snippet)。https://www.cbinsights.com/company/tylko/financials ; https://pitchbook.com/profiles/company/110583-64
- 2026 评测：书架 £450–3,500；交期"several weeks"；投诉：板材溢价、损坏件补发慢（一例 9 月→2 月）。https://rehaus.co/blogs/news/tylko-review
- 要点：10 年证明参数化到 CNC 能做到数千万欧元营收，但交期 3–6 周、10 倍 IKEA 价、最新融资是债。

### Emtek（Assa Abloy）— 五金行业最佳类比：assemble-to-order，非 fabricate-to-order
- "Orders typically ship within two to three business days"；部件全球采购，在洛杉矶按单组装。https://www.emtek.com/blog/Assembled-to-Order-in-LA/
- "mix and match finishes or styles at no additional upcharge"。https://www.emtek.com/our-story/assembled-in-la/
- 部分 made-to-order 饰面（Unlacquered Brass）加 2–3 天 (snippet)。
- 要点：Emtek 靠海外预饰面模块件 + 本地最终组装做到"定制 + 天级"。无本地切割、无本地饰面。

### 其他
- Rejuvenation：configured products 2–4 周 build + 2–10 工作日配送 (snippet)。https://www.rejuvenation.com/customer-service/shipping/
- Highland Forge：~3–4 周；93"–105" 加 $150。https://highlandforge.com/shipping/
- Curtarra：定宽窗帘杆 $159.20–199，any width（>82" 拼接），公差 3/8–3/4"，5 饰面同价。https://www.curtarra.com/products/john-custom-curtain-rods
- Continental Window Fashions：custom specialty rods 20–25 工作日 (snippet)。
- Opendesk（UK）：分布式 maker 家具；~2020 停止开源文件，关闭 Opendesk Express（一年），退出电商，转报价服务。https://en.wikipedia.org/wiki/Opendesk
- Hettich Plan：B2B 柜体配置器，非消费 AI。
- Zazzle ~$413M 2025 (第三方估计)；Nike By You 4–6 周，溢价 €20–40。
- Amazon Custom：Professional Seller 免费；Personalize / Configure / Assemble 三模式；≤5 surfaces、15 options/surface、100 options/product；可预览；订单数据售后转卖家 (snippets)。https://sell.amazon.com/programs/custom
- Etsy 定制金属门牌：2–3 周 / 4–10 工作日；RAW 比上色快；不锈钢定制报价"至少两倍" (snippets)。
- Etsy 黄铜毛巾杆：300–700 mm，"custom cuts available at no extra charge" (snippet)。

### AI / LLM 接单、拍照测量
- 未发现任何五金品牌用 LLM 接单。相邻：MEasure 给地板经销商拍照估价 (snippet)。
- Text-to-CAD：Zoo Text-to-CAD（2023-12）、AdamCAD（LLM 写 CadQuery/OpenSCAD）；Xometry Pro 测 7 工具。https://zoo.dev/blog/introducing-text-to-cad
- 含义：毛巾杆/支架不需要 text-to-CAD，只需 LLM 前端填 3–6 个参数进手工参数化模板（Tylko 路径）。

## 2. 按需制造网络

| 服务商 | 区域 | 起订 | 交期 | 饰面 | API |
|---|---|---|---|---|---|
| SendCutSend | US（Reno） | 无最小；≥$39 免运 | 304 SS 2–4 天；粉末 +3–5 天 | 15 色粉末含 Matte Black，无自定义色；阳极、电镀、攻丝、折弯、压铆 | 未公开 |
| OSH Cut | US（Utah） | — | 2 工作日；粉末 +4；全美 2 日达 | 17 色粉末；管激光即时 DFM | 未见 |
| Xometry | US/EU | 无 | 板切 3 工作日 | 阳极、电镀、粉末、钝化 | 有 developer.xometry.com |
| Fictiv | US/海外 | — | 钣金 as fast as 2 days | 未指明 | 未见 |
| Protolabs Network | US/EU | ~$100 起 (snippet) | as fast as 1 day | — | 未见 |
| Fractory | UK/US | 无；<£5,000 即时 | UK <9 工作日，加急 5 | 协调 | 未见 |
| Laserhub | DE/AT/CH | 最低 €80 (snippet) | 报价时显示；98% 可靠 | 粉末在标准菜单 | 有（WiCAM） |
| 247TailorSteel | NL/BE/DE/FR | 单件 | 1 分钟报价；48 h 起交付 | 去边、刻字、攻丝；无粉末 | 未披露 |

价格点：
- SendCutSend 粉末页：5052 铝 .187" 件 $20.69 @1 → $3.31 @100；冷轧钢 .119" 件 $73.26 @1 → $17.57 @100。https://sendcutsend.com/services/powder-coating/
- SendCutSend 规模：2025-10 营收破 $100M，+80% YoY；>30M 件、>300,000 客户；员工 410（2026-01）→ >500（2026-06）(snippets)。https://www.nnbw.com/news/2026/jan/28/
- 注：全是板/管激光 + 折弯；无人即时报价圆棒、焊接毛巾杆总成或装饰 PVD。

## 3. 难点
饰面
- 粉末（哑光黑）是唯一可在线即时报价的装饰饰面：SendCutSend +3–5 天（件 1"×3" 至 30"×36"）；OSH Cut +4 天。
- 独立小批粉末：Diamond Metal Finishing 3–5 天无最小；Cusack 24–48 h 加急；Fabworks 在线报价 (snippets)。
- PVD（拉丝镍/拉丝金/黑）是瓶颈：MASIC Industries "require a minimum order and are not available for single product coatings" (snippet)；Richter Precision Richkote 有 BHMA 标准饰面 (403)；Providence Metallizing 样品 1–2 周、生产 2–4 周 (snippet)。
- VaporTech（Masco 子公司）卖紧凑 VT i 系列小型 PVD 设备 (snippets)。https://blog.vaportech.com/blog-small-pvd-coating-system-2
- 含义：美/欧无任何 job shop 提供 qty-1 PVD 即时报价 + 天级交付。Emtek 模式正因此存在。

焊接 / 组装 / 攻丝：攻丝、压铆可即时报价；焊接仅 Xometry 报价引擎含，板切专家无即时焊接。

定制品退货：Amazon 自 2023-02-15 起 made-to-order/personalized 不可退，仅损坏/缺陷/材料不符 30 天内处理。https://www.valueaddedresource.net/amazon-to-stop-returns-on-custom-personalized-items/

## 4. 经济性
- 参照：KES 24" SUS304 拉丝毛巾杆（胶粘）Walmart $25.99 (snippet)。
- Home Depot ADA 不锈钢扶手 $10–200 (snippet)。
- 美国 job shop vs 中国工厂（Baosheng 自比，铝支架 .125"、4 折、6 攻丝、黑粉末）：SendCutSend ~$28.50 @10 / $21.30 @50 / $17.80 @100 / $15.20 @250；Baosheng ~$22.00 / $16.10 / $12.60 / $9.50（+$75 DAP 运费 @50）。盈亏平衡 ~50+ 件。https://baoshengindustry.com/resources/sheet-metal-fabrication/sendcutsend-vs-direct-sheet-metal-factory/
- 读法：qty 1–10 美国激光厂只贵 ~20–30%（运费前）且是天级；输在装饰饰面和组装的缺席。
- 定长溢价：Curtarra 各饰面同价、长度无加价；Etsy 黄铜毛巾杆 custom cuts 免费；Tylko ~10x IKEA；"1/5 愿多付 20%"无出处。
- 无定长卫浴五金专项调查。

## 5. 交付速度基准
| 供给 | 交期 |
|---|---|
| Amazon Prime 库存五金 | 1–2 天 |
| Emtek assemble-to-order | 2–3 工作日发货 |
| SendCutSend 不锈钢裸件 | 2–4 天（+3–5 粉末） |
| OSH Cut | 2 工作日；激光+攻丝+折弯+粉末 ≥5 工作日 |
| 247TailorSteel（EU） | 48 h 起 |
| Etsy 定制金属门牌 | 4–10 工作日至 2–3 周 |
| Rejuvenation configured | 2–4 周 + 2–10 天 |
| Highland Forge | 3–4 周 |
| Continental | 20–25 工作日 |
| Tylko | 3–6 周 |
| Nike By You | 4–6 周 |
模式：周内交付只有 (a) 裸件/粉末平板管件，或 (b) 预饰面部件本地组装。任何按单装饰电镀/PVD 都落在 3–5 周。

## 6. 失败/挣扎案例
- Shapeways（Ch.7 2024-07-02）：FY2023 营收 $34.5M、净亏 $43.9M、毛利 42%、现金 $12.2M；SPAC 增长压力；外协稀释质量控制；拒绝 $5M 救援；股价 $83.60 → $1.94。https://www.globenewswire.com/news-release/2024/03/28/2854506/ ; https://www.cadmore.com/blog/what-happened-to-shapeways
- Made.com（2022-11 破产管理）：IPO 估值 £775M；供应链让客户等数月；现金压在滞销库存。
- Interior Define（2022–23 资产出售给 Havenly）：付不起亚洲工厂和物流；货卡港口；300 → 115 人。https://businessofhome.com/articles/interior-define-bankruptcy-questions-answered
- Opendesk：关 Express、退出电商、停开源。
- Tylko（挣扎未败）：EIB 债务、裁员 9%、质量投诉。
教训：MTO 市场 42% 毛利扛不起固定开销；分布式外协伤一致性；海外 MTO 长链 = 客户不再容忍的交期 + 营运资金陷阱。

## (a) 对 KES 类品牌的可行性评估（agent 原文）
支持：1) 接单层便宜且成熟（Amazon Custom Configure/Assemble 免费；3–6 参数模板 = Tylko 滑块，非 text-to-CAD）；2) 裸件/粉末平板管件美国 2–4 天 qty 1 无 MOQ，EU 48 h–9 工作日；API 仅 Xometry、Laserhub 确认；3) qty 1–10 成本差 ~20–30%，加工经济性不是支架/通风口盖/门牌/搁架支架的阻碍。
反对：4) 装饰饰面是墙 —— 拉丝镍/金/黑 PVD qty 1 天级不存在；KES 核心是拉丝 SS/拉丝黄铜/哑光黑，只有哑光黑（粉末）快；现实架构是 Emtek 式：中国预饰面 + 本地切长/组装，"定制"限于长度+组合，不含表面；5) 毛巾杆/扶手 = 管 + 焊/压座 + 紧固件，无网络即时报价总成，需自有/合同微组装单元 —— 固定成本节点正是 Shapeways 和海外 MTO 的死因；6) 付费意愿证据弱 —— DTC 定长杆按平价卖，客户预期定长不加价；溢价在饰面/设计层；7) 所有成品 MTO 玩家 2–6 周，只有 assemble-to-order 做到天级；Amazon 定制不可退帮毛利但抬高测量错误成本。
结论：作为混合可行 —— (i) 中国预饰面模块件 + (ii) 美/欧切长与组装单元 + (iii) Amazon Custom/DTC 参数化配置器。不可行的是"AI → 本地造成品 PVD 毛巾杆 3 天"。最低风险试点：哑光黑粉末支架、通风口盖、门牌、搁架支架。EU 加工更快（48 h、Laserhub API）但同样 PVD 缺口。

## (b) 五大未知
1. 真实 KES 毛巾杆/扶手图纸在 SendCutSend/OSH Cut/Xometry/Laserhub 的 qty 1/10/100 即时报价与交期
2. 美/欧是否有小批装饰 PVD ≤5 天、每件最小量多少
3. 美国买家为定长卫浴五金付多少溢价
4. 美国 assemble-to-order 单元在 KES 量级的成本与盈亏平衡
5. Amazon Custom 参数化 SKU 在五金的转化与测量错误率
