import matplotlib.pyplot as plt
import numpy as np

def generate_data():
    """
    generate_data: 随机生成“年龄-身高”数据
    """    
    np.random.seed(seed=1)              # 固定随机数
    X_min = 4                           # X的下限，年龄的下限
    X_max = 30                          # X的上限，年龄的上限
    X_n = 16                            # 数据个数
    X = 5 + np.round(25 * np.random.rand(X_n), 2)    # 生成 16 个随机数，生成16个年龄数据

    Prm_c = [170, 108, 0.2]             # 生成参数
    T = np.round(Prm_c[0] - Prm_c[1] * np.exp(-Prm_c[2] * X) + 4 * np.random.randn(X_n), 2)  # 根据年龄随机生成身高数据
    np.savez('ch5_data.npz', X=X, X_min=X_min, X_max=X_max, x_n=X_n, T=T)       # 将生成的数据保存到 ch5_data.npz 文件中
