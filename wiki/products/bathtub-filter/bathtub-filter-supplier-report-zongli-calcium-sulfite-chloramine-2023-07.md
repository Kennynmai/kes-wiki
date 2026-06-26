---
type: supplier-report
status: active
owner: product
created: 2026-06-17
updated: 2026-06-17
visibility: company
confidence: low
officiality: supplier-provided
domain: product
domains: [bathtub-filter, chloramine, calcium-sulfite, supplier-report, zongli, media-testing]
source_count: 1
review_cycle: on-demand
verification_status: imported_unverified
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-chloramine-media-research.md
  - ./bathtub-filter-kes-media-eeat-and-clean-formula-narrative.md
  - ./bathtub-filter-claim-register.md
---

# 宗立 50g 亚硫酸钙球氯胺测试报告（2023-07）

## 资料定位
这是供应商提供的检测报告归档页，用于记录 **50g 宗立 2-3mm 亚硫酸钙球**在加标氯胺测试中的结果。

这份资料可以作为供应商筛选线索，但不能直接替代 KES 自己的 25 LPM bathtub-fill 条件台架测试，也不能直接支持面向消费者的强功效 claim。

raw 原件位置：

`C:\Users\KEVIN\Desktop\kes-wiki\raw\products\bathtub-filter\2026-06-17-zongli-calcium-sulfite-chloramine-test\`

## 原始报告信息
| 字段 | 内容 |
|---|---|
| 报告实体 | 淄博宗立新材料科技有限公司 |
| 样品编号 | `ZONET20230707001` |
| 样品接收时间 | 2023年07月07日 |
| 检测完成时间 | 2023年07月13日 |
| 样品名称 | 沐浴过滤器 |
| 检测项目 | 加标测试（氯胺） |
| 样品描述 | 内置滤料为 50g 宗立（2-3mm）亚硫酸钙球 |
| 流速 | 5 L/min、3 L/min |

## 检测结果摘录
| 测试点位 | 流速 | 检测项目 | 过滤前（mg/L） | 过滤后（mg/L） | 去除率 |
|---|---:|---|---:|---:|---:|
| 300L | 5 L/min | 一氯胺 | 0.46 | 0.0184 | 96% |
| 300L | 5 L/min | 三氯铵 | 1 | 0 | 100% |
| 500L | 5 L/min | 一氯胺 | 0.341 | 0.023 | 93.26% |
| 500L | 5 L/min | 三氯铵 | 0.728 | 0 | 100% |
| 300L | 3 L/min | 一氯胺 | 0.43 | 0 | 100% |
| 300L | 3 L/min | 三氯铵 | 1 | 0 | 100% |
| 500L | 3 L/min | 一氯胺 | 0.341 | 0 | 100% |
| 500L | 3 L/min | 三氯铵 | 0.728 | 0 | 100% |

## 对 KES 的含义
这份报告提供了一个值得验证的供应商信号：在 3-5 L/min、50g 亚硫酸钙球、300-500L 点位条件下，供应商报告显示一氯胺和原文所称“三氯铵”有高去除率。

但它目前不改变 [[bathtub-filter-chloramine-media-research]] 的主判断，原因是：
- 流速是 3 L/min 和 5 L/min，低于 KES bathtub filter 需要关注的高流量注水场景。
- 报告没有给出完整分析方法、检测限、重复次数、水温、pH、加标水制备方式和接触时间。
- 报告是供应商提供资料，不是 KES 自测或第三方认证报告。
- 原文写作 `三氯铵`，对外使用前需确认是否指 `三氯胺 / trichloramine`。

## 可用方式
内部可用：
- 作为宗立亚硫酸钙球供应商筛选资料。
- 作为 KES 后续氯胺 / 游离氯台架测试的对照线索。
- 作为询问供应商补充测试方法、检测限和第三方资质的依据。

暂不可用：
- 不可直接写成 “calcium sulfite removes chloramine at bathtub-fill flow rate”。
- 不可直接支持 Amazon / website 的消费者功效宣称。
- 不可替代 KES 25 LPM 去氯曲线或氯胺版台架测试。

## 待供应商补充问题
1. 原文 `三氯铵` 是否指 `三氯胺 / trichloramine`。
2. 检测方法名称、仪器或试剂盒型号、检测限。
3. 加标水制备方式、目标 pH、水温和是否含其他干扰物。
4. 每个点位是否有重复测试，是否有空白对照。
5. 300L / 500L 点位的定义：累计通水量还是采样体积。
6. 50g 亚硫酸钙球的填充体积、床层结构和实际接触时间。

## Raw 附件
- 原始 Word：`source-files\宗立测试-一氯胺及三氯铵 50g亚硫酸钙球.docx`
- 提取文本：`extracted-content.md`
- 签名/盖章图片：`extracted-assets\image-01.png`、`image-02.png`、`image-03.png`

注：当前环境未安装 LibreOffice/soffice，未生成 DOCX 页面渲染图；原始 DOCX 作为 source of record 保留。
