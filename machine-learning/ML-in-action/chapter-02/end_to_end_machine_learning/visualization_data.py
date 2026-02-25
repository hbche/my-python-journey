from pathlib import Path

import matplotlib.pyplot as plt
from load_data import load_housing_data

IMAGES_PATH = Path() / "images" / "end_to_end_project"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)


def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    """
    保存可视化结果
    """
    path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
    if tight_layout:
        # 如果紧凑布局的话，需要调用plt调整其布局为紧凑布局
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)


# 可视化数据集

plt.rc("font", size=14)
plt.rc("axes", labelsize=14, titlesize=14)
plt.rc("legend", fontsize=14)
plt.rc("xtick", labelsize=10)
plt.rc("ytick", labelsize=10)

housing = load_housing_data()
# 绘制每个特征值的直方图
# bins 用户控制直方图中每组，如果该参数为整数，表示将最大值到最小值这个范围均分成多少个区间；也可以设置为列表或数组，表示非均分区间；还可以设置为字符串，用于指定内置的分区策略。此处50，表示均分区间为50等份
# figsize 指定每个图形的宽高，为坐标轴、标签、图例等所有图形元素提供布局空间，本例中创建宽度为12英尺，高度为8英尺的图形画布。实际屏幕上展示的图形尺寸还需要结合DPI进行计算，即实际渲染的宽高为figsize * DPI
housing.hist(bins=50, figsize=(12, 8))
save_fig("attributes_histogram_plots")
plt.show()
