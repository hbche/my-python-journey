import matplotlib.pyplot as plt

decision_node = dict(boxstyle='sawtooth', fc='0.8')
leaf_node = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstyle='<-')

def create_plot():
    fig = plt.figure(1, facecolor='white')
    # 设置中文字体，防止中文乱码
    # Windows 系统使用 'SimHei'（黑体），macOS 使用 'Arial Unicode MS'
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False   # 正常显示负号
    fig.clf()
    create_plot.ax1 = plt.subplot(111, frameon=False)
    plot_node('决策节点', (0.5, 0.1), (0.1, 0.5), decision_node)
    plot_node('叶节点', (0.8, 0.1), (0.3, 0.8), leaf_node)
    plt.show()

def plot_node(node_text, center_pt, parent_pt, node_type):
    create_plot.ax1.annotate(node_text, xy=parent_pt, xycoords='axes fraction',
                            xytext=center_pt, textcoords='axes fraction',
                            va='center', ha='center',
                            bbox=node_type, arrowprops=arrow_args)
    
if __name__ == '__main__':
    create_plot()