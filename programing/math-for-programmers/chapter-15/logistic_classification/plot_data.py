import matplotlib.pyplot as plt


def plot_data(ds):
    plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
    plt.xlabel("里程数（英里）", fontsize=16)
    plt.ylabel("价格（美元）", fontsize=16)
    plt.scatter(
        [d[0] for d in ds if d[2] == 0], [d[1] for d in ds if d[2] == 0], c="C1"
    )
    plt.scatter(
        [d[0] for d in ds if d[2] == 1],
        [d[1] for d in ds if d[2] == 1],
        c="C0",
        marker="x",
    )
