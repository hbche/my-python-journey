import numpy as np
import matplotlib.pyplot as plt

def generate_regression_data(n_samples=100):
    # 设置随机种子，保证每次运行结果一致
    np.random.seed(42)
    
    # 特征 X：假设是广告投入（单位：万元），范围 0 到 10
    X = 10 * np.random.rand(n_samples, 1)
    
    # 目标 y：假设销售额 = 3.5 * 投入 + 10 + 噪声
    # 这里的 3.5 是权重(w)，10 是截距(b)
    noise = np.random.randn(n_samples, 1) * 2  # 添加标准差为 2 的高斯噪声
    y = 3.5 * X + 10 + noise
    
    return X, y

def plot_data(x_data, y_data):
    plt.figure(figsize=(8, 6))
    plt.scatter(x_data, y_data, color='blue', alpha=0.6, label='Data Points')
    plt.xlabel("Advertising Budget (X)")
    plt.ylabel("Sales (y)")
    plt.title("Relationship between Advertising and Sales")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def generate_linear_regression(w0, w1):
    def linear_regression(x):
        return w0 + w1 * x
    return linear_regression

default_w0 = np.random.rand()
default_w1 = np.random.rand()

def mse(x, y, linear_regression):
    return 0.5 * np.sum(y - linear_regression(x)) ** 2

def plot_args(w0_range, w1_range):
    w0_data = np.linspace(w0_range[0], w0_range[1], 100)
    w1_data = np.linspace(w1_range[0], w1_range[1], 100)
    plt.contour(w0_data, w1_data)
    
# 获取数据
X, y = generate_regression_data()
# plot_data(X, y)

print(f"X 的形状: {X.shape}")
print(f"y 的形状: {y.shape}")

def add_1(x):
    return x + 1