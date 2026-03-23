# 第 4 章 训练模型

目标：

1. 理解线性回归模型
2. 掌握训练模型的方法
   1. “闭式”方程
   2. 梯度下降算法
      1. 批量梯度下降
      2. 小批量梯度下降
      3. 随机梯度下降
3. 理解非线性模型
4. 掌握正则化技巧
5. 理解用于分类任务的两类模型
   1. 逻辑回归
   2. Softmax回归

## 4.1 线性回归模型

第一章介绍的根据收入中位数估算幸福指数是一个典型的线性回归问题：$life\_satisfaction=θ_0+θ_1\cdot{GDP\_per\_capita}$

公式 4-1：线性回归模型预测

$$
\hat{y} = θ_0 + θ_1x_1 + θ_2x_2 + ... +  θ_nx_n
$$

其中 $\hat{y}$为预测值，n为特征数量，$x_i$为第i个特征的值，$θ_j$为第j个模型参数，包括偏置参数$θ_0$和特征权重$θ_1$、$θ_2$、...、$θ_n$。

公式 4-2：线性回归模型预测（向量化形式）

$$
\hat{y} = h_θ(x) = θ \cdot{x}
$$

- θ 是模型的参数向量
- x 是特征向量

公式 4-3：线性回归模型的MSE代价函数

$$
MSE(X, h_θ)=\frac{1}{m}\sum_{i=1}^{m}(θ^TX_i - y_i)^2
$$

### 4.1.1 标准方程

为了找到最小化MSE的θ值，有一个闭式解方法，也就是一个直接得出结果的数学方程，即标准方程：

我们先从两个参数模型的 MSE 开始尝试通过计算偏导来计算参数θ的解：

$$
\frac{\delta{f}}{\delta{θ_i}} = \frac{2}{m}\sum_{i=1}^{m}(θ^TX_i-y_i)X_i=θ^T\frac{2}{m}\sum_{i=1}^{m}X_iX_i^T-\frac{2}{m}\sum_{i=1}^{m}y_iX_i
$$

令所有偏导都为 0 时对应的 MSE 就是最小的。从而可求得：

$$
θ^T\sum_{i=1}^{m}X_iX_i^T=\sum_{i=1}^{m}y_iX_i
$$

公式 4-4：标准方程

$$
\hat{θ} = \frac{X^Ty}{XX^T}
$$

- $\hat{θ}$：使代价最小的参数向量
- y：包含 1 到 m 的目标值向量

```py
def generate_data():
    """
    generate_data: 生成数据
    """
    np.random.seed(42)
    m = 100
    X = 2 * np.random.rand(m, 1)
    # 引入噪声
    Y = 4 + 3 * X + np.random.rand(m, 1)
    return X, Y


def plot_data(ax, X, Y):
    """
    plot_data: 绘制数据

    :param ax: 说明
    :param X: 说明
    :param Y: 说明
    """
    ax.scatter(X, Y, marker="o")
    ax.grid(True)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("y")


def calc_theta(X, Y):
    """
    calc_theta: 利用 MSE 标准方程的解，直接求解最佳参数

    :param X: 特征数据
    :param Y: 目标值
    """
    return np.linalg.inv((X.T @ X)) @ X.T @ Y


def plot_regression(ax: Axes, X, W):
    """
    plot_regression: 绘制线性回归函数

    :param ax: 说明
    :type ax: Axes
    :param X: 说明
    :param W: 说明
    """
    w0 = W[0]  # 偏置项
    w1 = W[1]
    Y = w0 + w1 * X
    (line,) = ax.plot(X, Y, color="black")
    line.set_label("Predict")
    ax.legend()
```

利用 scikit-learn 库求解：

```py
def calc_theta_by_scikit(X, Y):
    """
    calc_theta_by_scikit: 利用sklearn库中的线性回归模型计算参数

    :param X: 说明
    :param Y: 说明
    """
    lin_reg = LinearRegression()
    lin_reg.fit(X, Y)
    return lin_reg.intercept_, lin_reg.coef_
```

我们发现，两种计算方法计算出来的参数值是一样的：

```py
X, Y = generate_data()
m = 100
X_b = np.c_[np.ones((m, 1)), X]  # 添加 x_0 = 1 的偏置项
best_theta = calc_theta(X_b, Y)
print(f"Best Theta: {best_theta.reshape(2)}")
#  [4.51359766 2.98323418]
best_theta_2 = calc_theta_by_scikit(X_b, Y)
print(f"Best theta by sklearn: {best_theta_2}")
# Best theta by sklearn: (array([4.51359766]), array([[0.        , 2.98323418]]))
```

### 4.1.2 计算复杂度

标准方程计算 $X^TX$ 矩阵的逆矩阵时，是一个 (n+1)x(n+1) 的矩阵计算，涉及计算复杂度通常在$O(n^2.4)~O(n^3)$之间。如果特征数量翻倍，响应计算复杂度也会翻倍。
