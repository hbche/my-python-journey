import datetime
import json
import logging

from clean_and_analyze_data import clean_and_analyze_data, generate_price_trend_analysis
from config import TARGET_YEARS
from price_crawler import crawl_civic_prices


def main():
    """
    主程序入口
    """
    print("本田思域二手车价格抓取系统")
    print("=" * 50)

    try:
        # 1. 抓取数据
        print("正在抓取数据，请稍候...")
        car_data = crawl_civic_prices()

        if not car_data:
            print("警告：未能获取到有效数据")
            print("建议：")
            print("1. 检查网络连接")
            print("2. 验证目标网站是否可访问")
            print("3. 可能需要更新爬虫规则")
            return

        print(f"成功获取 {len(car_data)} 条原始数据")

        # 2. 清洗和分析数据
        print("正在清洗和分析数据...")
        df, yearly_stats, source_stats = clean_and_analyze_data(car_data)

        if df is not None:
            # 3. 保存数据到文件
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # 保存原始数据
            df.to_csv(
                f"civic_prices_raw_{timestamp}.csv", index=False, encoding="utf-8-sig"
            )

            # 保存统计结果
            yearly_stats.to_csv(
                f"civic_yearly_stats_{timestamp}.csv", encoding="utf-8-sig"
            )
            source_stats.to_csv(
                f"civic_source_stats_{timestamp}.csv", encoding="utf-8-sig"
            )

            # 保存JSON格式数据
            with open(f"civic_data_{timestamp}.json", "w", encoding="utf-8") as f:
                json_data = {
                    "metadata": {
                        "crawl_date": timestamp,
                        "total_records": len(df),
                        "target_years": TARGET_YEARS,
                    },
                    "data": df.to_dict("records"),
                }
                json.dump(json_data, f, ensure_ascii=False, indent=2)

            # 4. 生成分析报告
            print("\n" + "=" * 60)
            print("数据分析报告")
            print("=" * 60)

            analysis_report = generate_price_trend_analysis(df)
            print(analysis_report)

            # 保存分析报告
            with open(
                f"civic_analysis_report_{timestamp}.txt", "w", encoding="utf-8"
            ) as f:
                f.write(analysis_report)

            # 5. 显示关键统计信息
            print("\n关键统计信息：")
            print(yearly_stats)
            print("\n数据来源统计：")
            print(source_stats)

            print("\n数据已保存到以下文件：")
            print(f"1. 原始数据：civic_prices_raw_{timestamp}.csv")
            print(f"2. 年度统计：civic_yearly_stats_{timestamp}.csv")
            print(f"3. JSON数据：civic_data_{timestamp}.json")
            print(f"4. 分析报告：civic_analysis_report_{timestamp}.txt")

        else:
            print("数据清洗失败，请检查原始数据质量")

    except KeyboardInterrupt:
        print("\n用户中断程序")
    except Exception as e:
        print(f"程序执行出错: {e}")
        logging.error(f"主程序错误: {e}", exc_info=True)


if __name__ == "__main__":
    main()
