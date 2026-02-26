# 第 11 章 模拟力场

内容：
- 使用向量场和标量场对引力等力进行建模
- 使用梯度计算力向量
- 在Python中求函数的梯度
- 为小行星游戏添加重力场
- 在更高维度中计算梯度并处理向量场

## 11.5 用梯度连接能量和力

陡度的概念很重要，势能函数的陡度告诉我们一个对象向指定方向运动需要消耗多少能量。如你所料，向某方向移动所需的能量可以用于衡量方向相反的力。在本节余下的内容中，我们将对此进行深入研究。

正如本章开头提到的，梯度是一种运算，它接收像势能一样的标量场，并生成像引力场一样的向量场。在平面上的每一个位置$(x, y)$，梯度向量场都指向标量场增大最快的方向。本节将介绍如何计算标量场$U(x, y)$的梯度，这需要$U$分别对$x$和$y$求导。我们也会证明，一直在研究的势能函数$U(x,y)$的梯度是$-F(x, y)$，其中$F(x, y)$是在小行星游戏中实现的引力场。梯度这一概念将在本书的其余章节中广泛使用。

### 11.5.1 用横截面测量陡度

``` py
def u(x,y):
    """
    模拟
    """
    return 0.5 * (x**2 + y**2)

def scalar_field_contour(f,xmin,xmax,ymin,ymax,levels=None):

    fv = np.vectorize(f)

    X = np.arange(xmin, xmax, 0.1)
    Y = np.arange(ymin, ymax, 0.1)
    X, Y = np.meshgrid(X, Y)
    
    # https://stackoverflow.com/a/54088910/1704140
    Z = fv(X,Y)
    
    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, Z,levels=levels)
    ax.clabel(CS, inline=1, fontsize=10,fmt='%1.1f')
    plt.xlabel('x')
    plt.ylabel('y')
    fig.set_size_inches(7,7)
    
scalar_field_contour(u,-10,10,-10,10,levels=[10,20,30,40,50,60])
```