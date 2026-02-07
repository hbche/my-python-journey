import datetime
import logging

import pandas as pd


def clean_and_analyze_data(car_data):
    """
    清洗数据并进行统计分析
    """
    if not car_data:
        logging.warning("没有获取到有效数据")
        return None

    # 转换为DataFrame
    df = pd.DataFrame(car_data)

    # 数据清洗
    # 1. 移除重复数据
    df = df.drop_duplicates(subset=["year", "price", "source"], keep="first")

    # 2. 移除异常价格（假设价格在3-30万元之间为合理范围）
    df = df[(df["price"] >= 3) & (df["price"] <= 30)]

    # 3. 按年份分组统计
    yearly_stats = (
        df.groupby("year")
        .agg({"price": ["count", "mean", "min", "max", "std"], "source": "nunique"})
        .round(2)
    )

    yearly_stats.columns = [
        "样本数",
        "平均价格(万)",
        "最低价(万)",
        "最高价(万)",
        "价格标准差",
        "数据源数量",
    ]

    # 4. 按数据源统计
    source_stats = (
        df.groupby("source")
        .agg({"price": "count", "year": "nunique"})
        .rename(columns={"price": "数据量", "year": "覆盖年份数"})
    )

    return df, yearly_stats, source_stats


def generate_price_trend_analysis(df):
    """
    生成价格趋势分析报告
    """
    if df is None or df.empty:
        return "数据不足，无法生成分析报告"

    analysis_report = []
    analysis_report.append("=" * 60)
    analysis_report.append("本田思域（2021-2025年）二手车价格分析报告")
    analysis_report.append("=" * 60)
    analysis_report.append(f"分析时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    analysis_report.append(f"总数据量：{len(df)} 条")
    analysis_report.append("")

    # 按年份分析
    for year in sorted(df["year"].unique()):
        year_data = df[df["year"] == year]
        avg_price = year_data["price"].mean()
        price_range = f"{year_data['price'].min():.1f}-{year_data['price'].max():.1f}"
        sample_count = len(year_data)

        analysis_report.append(f"{year}年款思域：")
        analysis_report.append(f"  平均回收价：{avg_price:.2f} 万元")
        analysis_report.append(f"  价格区间：{price_range} 万元")
        analysis_report.append(f"  样本数量：{sample_count} 个")

        # 添加保值率分析（基于搜索结果中的保值率数据[2](@ref)[7](@ref)）
        if year == 2021:
            depreciation = "约63.5%（第二年保值率）"  # 根据搜索结果[2](@ref)[7](@ref)
        elif year == 2022:
            depreciation = "约57.5%（第三年保值率）"
        elif year == 2023:
            depreciation = "约51.8%（第四年保值率）"
        elif year == 2024:
            depreciation = "约46.3%（第五年保值率）"
        else:
            depreciation = "数据待补充"

        analysis_report.append(f"  预计保值率：{depreciation}")
        analysis_report.append("")

    # 总体趋势分析
    analysis_report.append("总体趋势分析：")
    analysis_report.append("1. 两厢思域市场紧缺，保值率较高[2](@ref)[7](@ref)")
    analysis_report.append("2. 1.5T版本溢价明显，比1.0T版本价格更高[6](@ref)")
    analysis_report.append(
        "3. 低里程（5万公里内）车辆比高里程车辆价格高1.5-2万元[6](@ref)"
    )
    analysis_report.append("4. 0过户记录车辆比过户1次的贵5%-8%[6](@ref)")
    analysis_report.append(
        "5. 车况良好的畅销车型，售价可达新车价80%-90%[2](@ref)[7](@ref)"
    )

    return "\n".join(analysis_report)
