---
type: source-capture
status: captured
owner: strategy
created: 2026-11-08
updated: 2026-11-08
visibility: company
confidence: medium
officiality: draft
domain: product-development
domains: [products, materials, quality-system, water-quality]
source_type: public-web-research
extraction_mode: targeted-search + quote-extraction
verification_status: spot-checked
---

# 浴室 Caddy 材料失效机理二次检索（2026-11-08）

## 检索目的

Kenny 追问：「引入金属材质能否解决这些问题——多孔渗色、酸性洗手液／牙膏酸蚀（密封剂只能防渗、不能防酸蚀）、硬水水垢、皂垢、发霉；以及太重、掉地上砸坏台面、运输崩边。」

目标：逐项核对**机理**，判断哪些是「材料属性问题」、哪些是「环境沉积问题」，并找出引入金属后**新出现**的失效模式。结论用于修订 `wiki/products/bathroom-caddy/bathroom-caddy-metal-first-hybrid-design-2026-11-08.md` 第 4 节，撤回上一版「六项均改善」的过度表述。

> 本文只保存检索到的事实、原文引文与明确标注的推断；**不含 KES 台架实测数据**。

---

## 一、石材：渗色与酸蚀

### 1. 酸蚀是化学反应，密封剂无效（事实，多方一致）

- Stone Shield Sydney《Marble etching, and how to stop it》 https://www.stoneshieldsydney.com/marble-etching
  > "An impregnating sealer works inside the stone, filling pores to slow absorption. The surface is still calcium carbonate, and acid still reacts with it."
  > "To stop etching, the acid has to be kept off the stone altogether. There are only two ways to do that: wipe every spill immediately, every time, or put a physical layer on top of the marble."
- Siamtak《How to Clean and Maintain Natural Stone Correctly》 https://en.siamtak.com/blog/how-to-clean-natural-stone
  > "An impregnating sealer primarily reduces the rate at which liquids enter the stone. It cannot stop the chemical reaction between acid and calcite that causes marble to etch."
- 化学式与台架数字（单一来源，供应商自测，标为参考值）：瑞丰源《Marble Etching in Kitchens: A 60-Day Acid Bench Test》 https://www.rfengyuan.com/news/marble-etching-in-kitchens-a-60-day-acid-bench-test-with-real-numbers
  - 反应：酸中的 H⁺ 攻击方解石 → 可溶钙盐 + H₂O + CO₂；**酸蚀是表面物质被溶解，不是污渍**。
  - 未密封抛光面：柠檬汁接触 45–60s 出现可见蚀痕；密封抛光面：约 4min。
  - 60 天每日酸滴：光泽度 82 GU → 41 GU；隔夜醋液蚀深约 38 μm。
  - 明确区分：**污渍在石头里，蚀痕是石头没了**（"a stain sits in the stone; an etch is the stone, gone"）。
- Natural Stone Institute  consumer 口径转引（Pistritto Marble）https://pistrittomarble.com/post/marble-countertops-hartford-ct
  > "a true sealer goes into the stone beneath the surface and prevents stains from going deep, but it does nothing to protect etching"
- 说明：花岗岩／真石英岩以硅酸盐为主，一般**不酸蚀**但仍可能渗色；大理石、石灰石、洞石、缟玛瑙含 CaCO₃，会酸蚀。**推断**：嵌片若改用致密微晶石／烧结石，可同时降低渗色与酸蚀，但须实测确认材质成分，不能按名称推断。

### 2. 「牙膏／洗手液是酸蚀源」这个口径需要纠正（事实）

- 《Acids and Bases in Your Home》pH 表 https://periodicelementtable.com/blog/household-acids-and-bases
  | 物品 | 典型 pH |
  |---|---|
  | 除垢剂（柠檬酸／氨基磺酸／磷酸／盐酸） | 1–3 |
  | 洁厕灵（常含盐酸） | 1–2 |
  | 洗手液（真皂，脂肪酸盐） | 9–10 |
  | pH 平衡沐浴／洗手产品 | 5–6 |
  | 牙膏（碳酸钙／水合硅石／氟化钠） | 7–9 |
  | 洗发水 | 5–7 |
  | 漂白剂（次氯酸钠） | 11–13 |
- Stone Shield Sydney 列举的浴室酸蚀源：柑橘、醋、酒、软饮、**浴室／厨房清洁喷雾**、**化妆品、香水、牙膏在台面上**（该来源把 toothpaste 列入 vanity 风险，但未区分是酸蚀还是研磨／残留）。
- **本库判断（推断）**：牙膏 pH 7–9，主要风险应是**研磨剂划伤抛光面 + 残留白膜**；真正的酸蚀主因是 pH 1–3 的除垢剂、洁厕灵、醋／柠檬酸清洁喷雾与部分化妆品。后续内容不得把「牙膏酸蚀」写成既定事实。

---

## 二、金属：耐酸，但怕氯离子

- British Stainless Steel Association《Selection of stainless steels for handling hydrochloric acid》 https://www.bssa.org.uk/topics.php?article=30
  > "The common stainless steel types, 304 and 316 should be considered non-resistant to hydrochloric acid at any concentration and temperature."
  > "Commercially available cleaning acids are around 16% hydrochloric acid... extremely aggressive to most stainless steel grades."
  > 建筑材料砂浆清洁剂（约 16% HCl）**溅到或酸雾**即可造成附近不锈钢件染色与点蚀；损伤初期表现为棕色锈斑，已形成点蚀则无法靠常规清洁修复。
- 《Stainless Steel Spray Types, Uses and Safe Steps》 https://evodyne.us/blogs/news/stainless-steel-spray（转引 BSSA 维护指南）
  > "For common 304/304L, it reports bleach concentrations of 5% or more can cause corrosion at room temperature, especially when the solution dries and becomes more concentrated."
  > 浓缩漂白剂不得接触装饰性不锈钢；即便稀释也须尽快冲洗。
- BJ Products《Is 304 stainless steel resistant to acid?》 https://bjproducts.net/is-304-stainless-steel-resistant-to-acid/
  > 304 对**稀薄、非氧化性有机酸**（醋酸、柠檬酸、稀硫酸、稀磷酸）室温下表现良好；失效条件是强酸、高温、**氯化物**（点蚀／缝隙腐蚀）。316 因含钼耐氯化物更佳。
- 国凯钢铁（中文，繁体）https://www.guokaisteel.com/page/news/show.aspx?num=2074
  > 304 对柠檬汁（pH 2–3）、白醋（pH 2.5–3）有基本抵抗力，但**长时间接触仍会腐蚀**；316 耐酸性显著提升。
- **本库判断（推断）**：日常洗手液／牙膏（pH 5–10）落在 304 的舒适区，故「方解石被溶解」这一机理确实消失；但风险**从怕弱酸转移为怕氯离子与强酸**，且后者是用户主动误用清洁剂造成。净改善真实，但必须靠 care card + 316 选项 + 误用测试兜底，不能宣称「耐酸」。

---

## 三、PVD 饰面：硬，但清洁禁忌多；哑黑最显水垢

- Bathroom Spare Parts《PVD finishes care》 https://www.bathroomspareparts.co.uk/account/help-centre-41-w.asp
  > "Avoid all acidic cleaners including limescale removers, vinegar, citric acid-based products, bleach, ammonia and bathroom cleaners containing these ingredients. While these products effectively dissolve limescale on chrome, they can attack PVD finishes, causing permanent discoloration, pitting or delamination."
  > "In hard water areas, dry taps after each use to prevent water spots from forming."
  > 常规清洁只用温水 + 超细纤维布；深度清洁用 pH 中性皂液，彻底冲洗并立即擦干；禁研磨工具与蜡／上光剂（哑光面会出亮斑）。错误清洁产品会使保修失效。
- INOXBATH《How to Properly Clean Stainless Steel Faucets》 https://www.inoxbath.com/news/inoxbath-guide-clean-stainless-steel-faucets-color-finishes
  > 黑色／深色 PVD：**避免酸性或含氯清洁剂**，仅用 pH 中性皂液与软布；硬水垢用湿布 + 温和洗涤剂，不得用研磨垫。
- FastFixer《Are Black Faucets Durable?》 https://fastfixer.blog/are-black-faucets-durable-finish-types-care
  > "Black faucets do not attract more hard water than chrome, but the high contrast between white calcium deposits and the dark matte surface makes spots significantly more visible."
  > 矿物含量与 fixture 颜色无关；哑黑的问题是**纯视觉对比**。白色斑点会被过度清洁，反而损伤涂层。
  > 拉丝／镀铬能靠反光掩饰轻微水点，哑黑不能。
- WellWhisk《Why Do Black Faucets Peel?》 https://wellwhisk.com/why-do-black-faucets-peel
  > 黑色龙头剥落的主因是**清洁习惯与水化学**：研磨工具、漂白剂／氨／酸、以及硬水矿物沉积长期不清理导致涂层起翘；涂层一旦分离无法重新结合。
  > 各品牌对醋的口径不一致：部分允许仅用于起泡器浸泡，多数禁止用于哑黑主体 —— 须以自家 care sheet 为准。
- **本库判断（关键推断）**：存在一个**反向组合陷阱**——哑黑 PVD 上白色 CaCO₃ 最显眼，而 PVD 又最怕能溶掉 CaCO₃ 的酸性除垢剂。因此「换金属 + 上哑黑 PVD」在硬水市场可能把「石材酸蚀」差评换成「涂层变色／剥落 + 保修争议」差评。这是上一版完全没覆盖的风险，须列为门禁项，并考虑把主推色从哑黑调整为拉丝／枪灰。

---

## 四、硬水水垢与皂垢：与基材无关

- 水垢：硬水中的 Ca²⁺/Mg²⁺ 随水滴蒸发留下碳酸盐沉积；pH 表（同上）给出 `CaCO₃ + 2H⁺ → Ca²⁺ + H₂O + CO₂`，说明酸能溶垢，也说明**垢是沉积物而非基材反应产物**。多家 PVD care 指南共同建议「用后擦干」，因为蒸发是成垢的必要环节。
- 皂垢：Wikipedia《Soap scum》 https://en.wikipedia.org/wiki/Soap_scum （镜像 http://sis.tdn.gtranslate.net/wiki/Soap_scum、https://www.wikiwand.com/en/Lime_soap）
  > "the white solid composed of calcium stearate, magnesium stearate, and similar alkaline earth metal derivatives of fatty acids. These materials result from the addition of soap and other anionic surfactants to hard water."
  > `2 C17H35COONa + Ca²⁺ → (C17H35COO)2Ca + 2 Na⁺`
- Biology Insights《What Is Soap Scum Made Of?》 https://biologyinsights.com/what-is-soap-scum-made-of-the-chemistry-explained
  > 不溶性金属皂干燥后强附着，**中性清洁剂难以去除，需酸来打破结合**；现代合成洗涤剂（syndets）不易生成皂垢。
- **本库判断（事实推论）**：水垢与皂垢的**生成量由水的硬度、皂的配方与蒸发决定，与托盘是石头还是金属无关**。金属能改变的是「附着力与可清洁性」（光滑非多孔、可拆洗），不是「是否生成」。因此上一版写「六项全部消除」对这两项不成立。
- **另一个反向风险（推断）**：皂垢通常需要酸才能分解，而 PVD 禁酸 —— 与第三节的死结同源。解法只能是「不让皂液在凹槽里停留 + 可拆下用中性清洁剂冲洗」。

---

## 五、发霉：金属不长霉，但界面会

- Fanno Creek《Can Mold Grow on Stainless Steel Surfaces?》 https://beavertondamagerestoration.com/can-mold-grow-on-stainless-steel-surfaces/
  > "mold can grow on stainless steel, though the metal itself is not a food source. Mold needs moisture, warmth, and organic material. Stainless steel surfaces often collect dust, grease, or soap scum, which provide the nutrients mold needs."
  > 霉斑常见于**边缘、接缝、角落、龙头底座、可拆件与垫圈下方**。
- DALILAI《Can Mold Grow on Stainless Steel?》 https://www.dll-hk.com/news/84
  > "The mold is usually growing on the residue covering the metal rather than on the stainless steel itself."
  > 重点检查部位：螺钉头、把手底座、铰链板、**橡胶垫圈**、玻璃夹、墙面支架、凹槽把手；"water remains trapped behind a mounting plate, gasket, bracket, or decorative cover"。
  > "The stainless steel grade does not prevent mold when the surface remains dirty and wet."
- Biology Insights https://biologyinsights.com/can-mold-grow-on-steel-how-it-happens-how-to-stop-it
  > 钢、玻璃、混凝土等无机材料不能被霉菌代谢；霉菌吃的是表面积累的有机物。温暖潮湿空气遇冷金属表面会**结露**，提供水分。
- Oceanside《Can Mold Grow on Metal or Glass Surfaces?》 https://oceansidedamagerestoration.com/?p=1290
  > 控制手段是擦干、清除有机膜、通风、消除持续湿源，而非更换材料。
- **本库判断（关键推断）**：混合结构的「可拆嵌片 + 卡扣 / 磁吸 + 硅胶圈 + 脚垫」会引入比整块石头**更多的滞水界面**。若用结构胶、做封闭腔、或硅胶圈长期泡水，发霉风险可能**高于**全石方案。因此发霉是**装配纪律问题**（无胶、开敞、可拆、可干燥），不是金属带来的收益；这一项必须在 RFQ 与高湿舱测试中单列。

---

## 六、物理问题：减重的收益与新增失效（均为推断，须实测）

| 原差评 | 金属方案的作用 | 新增／未解决 |
|---|---|---|
| 太重 | 薄壁金属 + 3–4mm 嵌片，估算 0.8–1.2kg → 0.35–0.55kg（沿用简报估算，未实测） | 薄壁手感可能「轻飘」，需局部配重（呼应 RV 龙头项目「更重但不更好装」教训） |
| 砸坏台面 | 减重降低冲击 | 金属折边更硬更薄，裸边反而可能刮花／磕裂台面；必须软脚垫 + 卷边 + R 角。**这是结构收益，不是材料收益** |
| 运输崩边 | 金属包边、嵌片变小、可单独补发 | 薄壁冲压盘受压会**永久凹陷／折边变形导致嵌片卡死**（整件报废，不同于石头局部崩边）；PVD 划伤。须做堆码与运输完整性测试 |

- 冷凝假设：金属导热远快于石材，湿热浴室中冷表面可能更易结露、延长湿润时间（来源见 Biology Insights 关于金属表面结露的通用描述）。**未做台架验证，仅列为待验证假设**，不得写入对外结论。

---

## 七、本次检索带来的结论修正（写回 wiki 的要点）

1. 撤回「六项均改善」「C 六项全部消除」。8 项按机理分三类：材料属性（可换材料解决）、环境沉积（换材料无效）、界面卫生（靠装配，且可能反噬）。
2. **水垢／皂垢与基材无关**，金属不解决；哑黑 PVD 上水垢更显眼，且 PVD 禁酸洗 ⇒ 新出现「过度清洁 → 涂层损坏 → 保修争议」链路。
3. 酸蚀收益真实，但**风险从怕弱酸转移为怕氯离子／强酸**（BSSA：304/316 不耐受盐酸；≥5% 漂白剂室温可致腐）。
4. 纠正「牙膏／洗手液酸蚀」口径：pH 7–9 / 5–6，非主要酸蚀源；真凶是 pH 1–3 除垢剂与洁厕灵。
5. 发霉靠装配纪律，混合结构界面更多，设计不当会更糟。
6. 真正的杠杆是「不积水 + 可拆洗 + 快干」；金属的价值是把这套结构做得薄、精确、耐久、可同色。
7. 与 KES 软水主线的关联**仅为内容与叙事协同**（共同变量 Ca²⁺/Mg²⁺），不是技术／供应链协同，不改变「不作为独立新品类立项」结论。

---

## 八、待验证清单

- 买样实测：尺寸、重量、凹槽深度／直径、瓶底直径、密封剂、抛光或哑光。
- 台架：硬水循环 + 擦干／不擦干对照；哑黑与拉丝的水垢视觉评级与擦拭复净率；pH1–3 除垢剂与含氯清洁剂误用后的点蚀／涂层检查；高湿舱后拆开检查缝隙与硅胶圈；堆码后薄壁平整度与嵌片拆装；台面划痕／磕裂。
- 市场：SellerSprite / Helium10 差评词云增列 `water spots`、`hard water stains`、`mold`、`dented`、`finish peeling`，验证这些新风险在真实评论里的权重。
- 供应商：确认嵌片材质成分（微晶石／烧结石是否含 CaCO₃）、PVD 厂家 care sheet 与保修条款、哑黑 vs 拉丝的 Ra 与可清洁性数据。

---

## Sources（全部为 2026-11-08 公开检索）

1. https://www.bssa.org.uk/topics.php?article=30
2. https://evodyne.us/blogs/news/stainless-steel-spray
3. https://bjproducts.net/is-304-stainless-steel-resistant-to-acid/
4. https://www.guokaisteel.com/page/news/show.aspx?num=2074
5. https://www.bathroomspareparts.co.uk/account/help-centre-41-w.asp
6. https://www.inoxbath.com/news/inoxbath-guide-clean-stainless-steel-faucets-color-finishes
7. https://fastfixer.blog/are-black-faucets-durable-finish-types-care
8. https://wellwhisk.com/why-do-black-faucets-peel
9. https://faucettaps.com/how-to-clean-luxury-faucets-without-damaging-the-finish
10. https://www.stoneshieldsydney.com/marble-etching
11. https://en.siamtak.com/blog/how-to-clean-natural-stone
12. https://www.rfengyuan.com/news/marble-etching-in-kitchens-a-60-day-acid-bench-test-with-real-numbers
13. https://pistrittomarble.com/post/marble-countertops-hartford-ct
14. https://dynamicstonetools.net/blog/stone-fabrication-news-guides-16/marble-in-the-kitchen-myth-vs-reality-220
15. https://periodicelementtable.com/blog/household-acids-and-bases
16. https://en.wikipedia.org/wiki/Soap_scum
17. https://biologyinsights.com/what-is-soap-scum-made-of-the-chemistry-explained
18. https://beavertondamagerestoration.com/can-mold-grow-on-stainless-steel-surfaces/
19. https://www.dll-hk.com/news/84
20. https://biologyinsights.com/can-mold-grow-on-steel-how-it-happens-how-to-stop-it
21. https://oceansidedamagerestoration.com/?p=1290
