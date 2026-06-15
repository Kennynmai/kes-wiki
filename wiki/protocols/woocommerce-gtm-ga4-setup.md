# WooCommerce + GTM + GA4 接入完整指南

> 针对浴室五金 DTC 品牌 | 实现 YouTube/Pinterest 转化闭环追踪

---

## 一、整体架构（先理解再动手）

```
[YouTube/Pinterest 内容]
        ↓（带 UTM 参数）
[WooCommerce 独立站]
        ↓（GTM 部署追踪代码）
[GA4 收集数据]
        ↓（事件追踪：浏览/加购/购买）
[你看到报告：哪个渠道带来了多少订单]
```

**三个工具各自的职责：**

| 工具 | 职责 | 是否需要 |
|------|------|---------|
| **GA4** | 接收并分析数据 | ✅ 必须 |
| **GTM** | 部署 GA4 追踪代码到 WC 网站 | ✅ 强烈推荐 |
| **GTM4WP 插件** | 让 GTM 自动追踪 WooCommerce 电商事件 | ✅ 强烈推荐 |

---

## 二、方案一：使用 GTM4WP 插件（★ 推荐）

> 最适合非技术用户，自动追踪所有 WooCommerce 电商事件

### Step 1：安装并配置 GTM4WP 插件

**操作路径：** WordPress 后台 → 插件 → 安装插件 → 搜索 "GTM4WP"

| 步骤 | 操作 |
|------|------|
| ① | 搜索 **"GTM4WP"**（全名：*GTM4WP - Google Tag Manager for WordPress*） |
| ② | 安装并启用 |
| ③ | 进入 **设置 → Google Tag Manager** |
| ④ | 填入你的 **GTM Container ID**（格式：`GTM-XXXXXX`）|
| ⑤ | 勾选 **"Compatibility Mode"**（避免与其他插件冲突）|
| ⑥ | 保存 |

**GTM Container ID 在哪里找？**
```
登录 tagmanager.google.com
→ 右上角点击 Container 名称
→ 复制 "GTM-XXXXXX" 格式的 ID
```

---

### Step 2：在 GTM4WP 中开启 WooCommerce 追踪

**操作路径：** WordPress 后台 → 设置 → Google Tag Manager → **Events**

| 设置项 | 是否开启 | 说明 |
|--------|---------|------|
| **Basic eCommerce Events** | ✅ 开启 | 自动追踪：产品浏览、加购物车、移除购物车、结账开始、购买完成 |
| **Enhanced eCommerce** | ✅ 开启 | 追踪：产品印象、点击、促销曝光/点击 |
| **User ID tracking** | ⚠️ 可选 | 登录用户追踪（如果有会员系统）|
| **Cart Data Layer** | ✅ 开启 | 购物车数据推送到 dataLayer |

**开启后，GTM4WP 会自动向网页注入 `dataLayer` 事件：**
```javascript
// 用户浏览产品页时，自动推送：
dataLayer.push({
  'event': 'view_item',
  'ecommerce': {
    'items': [{
      'item_id': 'GB-24-BB',
      'item_name': '24" Matte Black Grab Bar',
      'price': 89.99,
      'quantity': 1
    }]
  }
});
```

---

### Step 3：在 GTM 中配置 GA4 电商事件

**操作路径：** [tagmanager.google.com](https://tagmanager.google.com) → 你的 Container → **Tags**

#### 3.1 添加 GA4 Configuration Tag（配置标签）

| 设置项 | 值 |
|--------|-----|
| **Tag Type** | Google Analytics: GA4 Configuration |
| **Measurement ID** | 你的 GA4 Measurement ID（格式：`G-XXXXXXX`）|
| **Trigger** | All Pages |
| **Name** | `GA4 - Config` |

**GA4 Measurement ID 在哪里找？**
```
登录 analytics.google.com
→ 左下角 ⚙️（管理）→ 数据流 → 选择你的网站数据流
→ 复制 "Measurement ID"（格式：G-XXXXXXX）
```

#### 3.2 添加 GA4 Event Tag（电商事件标签）

因为 GTM4WP 已经自动推送了 `dataLayer` 事件，**你不需要手动配置每个事件**—— 只需要开启 GA4 的 Enhanced Ecommerce 即可：

| 设置项 | 值 |
|--------|-----|
| **Tag Type** | Google Analytics: GA4 Event |
| **Configuration Tag** | 选择上面创建的 `GA4 - Config` |
| **Event Name** | 留空（自动从 dataLayer 读取）|
| **Trigger** | **无需手动设置**，GA4 自动读取 dataLayer |
| **Name** | `GA4 - EEC - Auto-Track` |

**更简单的方法（推荐）：**

直接在 GA4 Configuration Tag 中勾选：
```
✅ Enable Enhanced Ecommerce Features (EEC)
```
这样就**自动追踪所有 WooCommerce 电商事件**，无需单独配置 Event Tag。

---

### Step 4：验证数据是否正常收集

**方法 1：使用 GTM Preview 模式**
```
1. 在 GTM 中点击右上角 "Preview"
2. 输入你的 WC 网站 URL
3. 在打开的网站中浏览产品 → 加购物车 → 结账
4. 回到 GTM Preview 窗口，查看 Events 标签
   → 应该看到：view_item, add_to_cart, begin_checkout, purchase
```

**方法 2：使用 GA4 DebugView**
```
1. 在 GA4 后台 → 左下角 ⚙️ → 调试视图（DebugView）
2. 在 WC 网站上进行操作（浏览产品、加购等）
3. 实时看到事件是否被正确追踪
```

**方法 3：查看 GA4 报告（延迟 24-48h）**
```
GA4 后台 → 报告 → 变现 → 电商购买
→ 应该看到产品名称、销售额、订单数
```

---

## 三、方案二：手动部署（适合有技术能力的用户）

> 如果不想装插件，可以手动在 WC 主题中添加代码

### Step 1：获取 GTM 代码片段

```
登录 tagmanager.google.com
→ 右上角点击 Container ID（GTM-XXXXXX）
→ 复制两段代码：
   - <head> 部分代码（放在 <head> 标签内）
   - <body> 部分代码（放在 <body> 标签后立即）
```

### Step 2：将 GTM 代码添加到 WooCommerce 主题

**操作路径：** WordPress 后台 → 外观 → 主题文件编辑器 → 选择 `header.php`

```php
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':...})</script>
    <!-- End Google Tag Manager -->
    <?php wp_head(); ?>
</head>
<body>
    <!-- Google Tag Manager (noscript) -->
    <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXX" ...></iframe>
    <!-- End Google Tag Manager (noscript) -->
```

⚠️ **注意：** 修改主题文件前**务必备份**，或改用子主题（Child Theme）。

### Step 3：手动添加 dataLayer 电商事件

需要在 WooCommerce 的模板文件中手动添加 `dataLayer.push()` 代码，**工作量较大，不推荐**。

→ **建议直接使用方案一（GTM4WP 插件）**

---

## 四、WooCommerce 必须追踪的电商事件清单

| 事件名称 | 触发时机 | 对你的意义 |
|---------|---------|-----------|
| `view_item` | 用户浏览产品详情页 | 哪个产品被看最多？ |
| `add_to_cart` | 用户点击"加入购物车" | 哪个渠道带来的用户加购率最高？ |
| `begin_checkout` | 用户进入结账页 | 结账流失率？ |
| `purchase` | 用户完成付款 | **核心指标：哪个渠道带来最多订单？** |
| `view_item_list` | 用户浏览产品列表页 | 哪个产品展示最多？ |
| `select_item` | 用户从列表中点击产品 | 产品列表的点击率？ |

**GA4 中查看这些事件：**
```
GA4 后台 → 报告 → 变现 → 电商购买
→ 或：探索 → 自由格式 → 维度：事件名称，指标：事件数
```

---

## 五、UTM 参数 + WC 订单归因配置

### 5.1 UTM 参数规范（YouTube/Pinterest → WC）

**YouTube 描述区链接格式：**
```
https://yourstore.com/product/grab-bar/?utm_source=youtube
&utm_medium=video
&utm_campaign=grabbar_safety
&utm_content=longform_001
```

**Pinterest Pin 链接格式：**
```
https://yourstore.com/product/grab-bar/?utm_source=pinterest
&utm_medium=pin
&utm_campaign=bathroom_safety
&utm_content=freshpin_001
```

### 5.2 在 WC 订单详情中显示 UTM 来源

**安装插件：WooCommerce Google Analytics Pro（可选）**

或添加以下代码到 `functions.php`（子主题中）：
```php
// 将 UTM 参数保存到 WC 订单中
add_action('woocommerce_checkout_create_order', function($order, $data) {
    $utm_fields = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content'];
    foreach ($utm_fields as $field) {
        if (isset($_COOKIE[$field])) {
            $order->update_meta_data('_' . $field, sanitize_text_field($_COOKIE[$field]));
        }
    }
}, 10, 2);
```

> ⚠️ 需要先将 UTM 参数保存为 Cookie（可以用 GTM 的 Cookie 变量实现）

---

## 六、GA4 中查看 YouTube/Pinterest 转化数据

### 6.1 查看流量来源报告

```
GA4 后台
→ 报告 → 获客 → 流量获取
→ 维度：会话默认渠道组 / 会话来源 / 会话媒介
→ 可以看到：
   - youtube / video（YouTube 长视频）
   - pinterest / pin（Pinterest Pins）
   - (direct) / (none)（直接流量，可能是 Dark Social）
```

### 6.2 查看转化事件

```
GA4 后台
→ 报告 → 变现 → 电商购买
→ 或：报告 → 互动度 → 事件
→ 搜索：purchase
→ 查看 "事件数" 和 "事件价值"
```

### 6.3 建立自定义受众（用于再营销）

```
GA4 后台 → 右上角 ⚙️ → 受众 → 新建受众
→ 条件：
   - 来源 = youtube  且  未完成购买 → "YouTube 弃单用户"
   - 来源 = pinterest  且  未完成购买 → "Pinterest 弃单用户"
→ 可用于 Google Ads 再营销
```

---

## 七、与 YouTube/Pinterest 内容营销的整合

### 7.1 YouTube 描述区链接（带 UTM）

```
💧 安全扶手完整测评 + 安装教程（长视频）
👉 https://yourstore.com/grab-bar?utm_source=youtube&utm_medium=video&utm_campaign=grabbar_review

📦 同款产品在 Amazon 购买
👉 https://amazon.com/your-product?tag=yourtag（Amazon Attribution Tag）
```

### 7.2 Pinterest Rich Pins 设置

```
Pinterest 商家后台 → 设置 → Rich Pins
→ 验证 WC 网站（需要添加 meta 标签到头部）
→ 启用后，Pin 会自动显示价格 + 库存状态
```

**WC 需要安装插件：Pinterest for WooCommerce**
```
WordPress 后台 → 插件 → 安装插件 → 搜索 "Pinterest for WooCommerce"
→ 安装并连接 Pinterest 商家账户
→ 自动同步产品目录到 Pinterest Catalog
```

---

## 八、常见问题 & 避坑指南

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| GA4 看不到电商事件 | GTM4WP 未开启 EEC | 检查 GTM4WP 设置 → Events → 勾选 Enhanced Ecommerce |
| UTM 参数丢失 | 用户跳转时 WC 使用了重定向 | 使用 GTM 捕获 UTM 并写入 Cookie（留存 7 天）|
| Purchase 事件重复计数 | WC 感谢页刷新 | GTM4WP 默认防重复，无需处理 |
| GA4 数据延迟 | 正常延迟 24-48h | 使用 DebugView 实时验证 |
| Pinterest 成交无法追踪 | 用户从 Pin → Amazon 直接购买 | 使用 Amazon Attribution Tag（见之前方案）|

---

## 九、执行优先级

| 阶段 | 任务 | 预计耗时 |
|------|------|---------|
| **Phase 0** | 安装 GTM4WP 插件 + 填入 GTM ID | 15 分钟 |
| **Phase 1** | 在 GTM 中配置 GA4 Configuration Tag | 30 分钟 |
| **Phase 2** | 使用 GTM Preview 验证事件追踪 | 30 分钟 |
| **Phase 3** | 在 GA4 中设置转化目标（purchase 事件）| 15 分钟 |
| **Phase 4** | YouTube/Pinterest 链接统一 UTM 规范 | 1 小时 |
| **Phase 5** | 建立 GA4 自定义报告（渠道 × 转化率）| 30 分钟 |

**总计：约 3 小时完成基础配置。**

---

## 十、下一步行动

- [ ] ① 确认已有 GA4 账户 + Measurement ID（没有的话先创建）
- [ ] ② 确认已有 GTM 账户 + Container ID（没有的话先创建）
- [ ] ③ 安装 GTM4WP 插件并填入 GTM Container ID
- [ ] ④ 在 GTM 中配置 GA4 Configuration Tag（开启 EEC）
- [ ] ⑤ 使用 Preview 模式验证 `view_item` / `add_to_cart` / `purchase` 事件
- [ ] ⑥ 统一 YouTube/Pinterest 的 UTM 参数规范
- [ ] ⑦ 在 GA4 中查看"流量获取"报告，确认来源数据正常

---

*文档创建：2026-06-02*
*适用对象：浴室五金 DTC 品牌（WooCommerce 独立站）*
*关联文档：inbox/conversion-loop-technical-guide.md*
