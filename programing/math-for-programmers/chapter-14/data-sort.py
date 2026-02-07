"""
CSV文件排序脚本
功能：读取本地CSV文件，按里程数排序，输出为新的CSV文件
作者：基于搜索结果编写
日期：2026-02-06
"""

import csv
import os
from pathlib import Path

import pandas as pd

header_map = {
    "": "mileage",
    "": "price"
}


def sort_csv_by_mileage_pandas(
    input_file, output_file, mileage_column="里程(万公里)", ascending=True
):
    """
    使用pandas库对CSV文件按里程数排序（推荐方法）

    参数：
    input_file: 输入CSV文件路径
    output_file: 输出CSV文件路径
    mileage_column: 里程数列名，默认为'里程(万公里)'
    ascending: 排序顺序，True为升序，False为降序
    """
    try:
        # 1. 读取CSV文件
        print(f"正在读取文件: {input_file}")
        df = pd.read_csv(input_file, encoding="utf-8")

        # 2. 检查里程数列是否存在
        if mileage_column not in df.columns:
            available_columns = ", ".join(df.columns)
            raise ValueError(
                f"列 '{mileage_column}' 不存在。可用列: {available_columns}"
            )

        # 3. 数据清洗：处理缺失值和数据类型转换
        print("正在进行数据清洗...")
        # 检查缺失值
        missing_count = df[mileage_column].isnull().sum()
        if missing_count > 0:
            print(f"警告：发现 {missing_count} 个缺失值，将删除包含缺失值的行")
            df = df.dropna(subset=[mileage_column])

        # 尝试转换为数值类型
        try:
            df[mileage_column] = pd.to_numeric(df[mileage_column], errors="coerce")
            # 再次检查转换后的缺失值
            df = df.dropna(subset=[mileage_column])
        except Exception as e:
            print(f"数据类型转换警告: {e}")

        # 4. 按里程数排序
        print(f"正在按'{mileage_column}'进行{'升序' if ascending else '降序'}排序...")
        sorted_df = df.sort_values(by=mileage_column, ascending=ascending)

        # 5. 输出到新的CSV文件
        sorted_df.to_csv(output_file, index=False, encoding="utf-8")
        print(f"排序完成！结果已保存到: {output_file}")
        print(f"原始数据行数: {len(df)}，排序后数据行数: {len(sorted_df)}")

        # 6. 显示排序后的前几行数据
        print("\n排序后的前5行数据:")
        print(sorted_df.head())

        return sorted_df

    except FileNotFoundError:
        print(f"错误：文件 '{input_file}' 未找到")
        return None
    except Exception as e:
        print(f"处理过程中发生错误: {e}")
        return None


def sort_csv_by_mileage_csv_module(
    input_file, output_file, mileage_column_index=1, ascending=True
):
    """
    使用内置csv模块对CSV文件按里程数排序（适用于简单场景）

    参数：
    input_file: 输入CSV文件路径
    output_file: 输出CSV文件路径
    mileage_column_index: 里程数列的索引（0-based）
    ascending: 排序顺序，True为升序，False为降序
    """
    try:
        # 1. 读取CSV文件
        print(f"使用csv模块读取文件: {input_file}")
        with open(input_file, "r", newline="", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            header = next(reader)  # 读取标题行
            data = list(reader)

        # 2. 检查列索引是否有效
        if mileage_column_index >= len(header):
            raise ValueError(
                f"列索引 {mileage_column_index} 超出范围。文件共有 {len(header)} 列"
            )

        # 3. 按指定列排序
        print(
            f"正在按第{mileage_column_index + 1}列('{header[mileage_column_index]}')排序..."
        )

        # 过滤并转换数据
        filtered_data = []
        for row in data:
            if len(row) > mileage_column_index and row[mileage_column_index].strip():
                try:
                    # 尝试转换为浮点数
                    mileage_value = float(row[mileage_column_index])
                    filtered_data.append((mileage_value, row))
                except ValueError:
                    print(f"警告：跳过无法转换为数字的行: {row}")

        # 排序
        sorted_data = sorted(filtered_data, key=lambda x: x[0], reverse=not ascending)

        # 4. 写入新的CSV文件
        with open(output_file, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            for _, row in sorted_data:
                writer.writerow(row)

        print(f"排序完成！结果已保存到: {output_file}")
        print(f"处理了 {len(sorted_data)} 行有效数据")

        return sorted_data

    except Exception as e:
        print(f"处理过程中发生错误: {e}")
        return None


def batch_process_csv_files(input_folder, output_folder, mileage_column="里程(万公里)"):
    """
    批量处理文件夹中的所有CSV文件

    参数：
    input_folder: 输入文件夹路径
    output_folder: 输出文件夹路径
    mileage_column: 里程数列名
    """
    try:
        # 创建输出文件夹
        Path(output_folder).mkdir(parents=True, exist_ok=True)

        # 获取所有CSV文件
        csv_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".csv")]

        if not csv_files:
            print(f"在文件夹 '{input_folder}' 中未找到CSV文件")
            return

        print(f"找到 {len(csv_files)} 个CSV文件，开始批量处理...")

        results = []
        for csv_file in csv_files:
            input_path = os.path.join(input_folder, csv_file)
            output_path = os.path.join(output_folder, f"sorted_{csv_file}")

            print(f"\n处理文件: {csv_file}")
            result = sort_csv_by_mileage_pandas(input_path, output_path, mileage_column)

            if result is not None:
                results.append(
                    {"file": csv_file, "rows": len(result), "output": output_path}
                )

        # 输出批量处理摘要
        print("\n" + "=" * 50)
        print("批量处理完成摘要:")
        print("=" * 50)
        for res in results:
            print(
                f"文件: {res['file']} -> 输出: {os.path.basename(res['output'])} (行数: {res['rows']})"
            )

    except Exception as e:
        print(f"批量处理错误: {e}")


def main():
    """主函数：演示脚本的使用方法"""
    print("=" * 60)
    print("CSV文件排序脚本")
    print("功能：按里程数对CSV文件进行排序")
    print("=" * 60)

    # 示例文件路径（请根据实际情况修改）
    input_file = "思域二手车数据.csv"  # 您的CSV文件路径
    output_file_pandas = "思域二手车数据_按里程排序.csv"
    output_file_csv = "思域二手车数据_按价格排序.csv"

    # 方法1：使用pandas库（推荐）
    print("\n方法1：使用pandas库处理（推荐）")
    print("-" * 40)
    sort_csv_by_mileage_pandas(
        input_file=input_file,
        output_file=output_file_pandas,
        mileage_column="里程(万公里)",  # 根据您的CSV列名调整
        ascending=True,  # True为升序，False为降序
    )

    # 方法2：使用csv模块
    print("\n方法2：使用内置csv模块处理")
    print("-" * 40)
    sort_csv_by_mileage_csv_module(
        input_file=input_file,
        output_file=output_file_csv,
        mileage_column_index=2,  # 假设里程数在第2列（0-based索引）
        ascending=True,
    )

    # 批量处理示例（如果需要）
    # input_folder = "原始数据"
    # output_folder = "排序后数据"
    # batch_process_csv_files(input_folder, output_folder, '里程(万公里)')

    print("\n" + "=" * 60)
    print("脚本执行完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
