---
name: analyzing-marketing-campaign
description: 分析多渠道数字营销数据，计算转化漏斗、效率指标，并给出预算调整建议。
input:
    - file: Excel/CSV，包含Date, Campaign_Name, Channel, Impressions, Clicks, Conversions, Spend, Revenue, Orders等字段
output:
    - Markdown/Excel表格，含各项指标与建议
---

## 任务流程
1. 读取Excel/CSV数据。
2. 计算各渠道CTR（点击率）、CVR（转化率）。
3. 计算ROAS（广告回报率）、CPA（获客成本）、净利润等效率指标。
4. 输出对比表格，生成分析解读与预算建议。

## 公式示例
- CTR% = Clicks / Impressions * 100
- CVR% = Conversions / Clicks * 100
- ROAS = Revenue / Spend
- CPA = Spend / Conversions
- Net Profit = Revenue - (Spend + 其他成本)