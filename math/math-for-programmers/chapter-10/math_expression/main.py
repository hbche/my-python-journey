import math

import matplotlib.pyplot as plt
import numpy as np
from expressions import (
    Negative,
    Number,
    Power,
    Sum,
    Variable,
)

# 将数学函数(3x**2 + x)*sin(x)转换成表达式

# f_expression = Product(
#     Sum(Product(Number(3), Power(Variable("x"), Number(2))), Variable("x")),
#     Apply(Function("sin"), Variable("x")),
# )

# # 计算表达式包含的变量
# # f_expression = Power(Variable("x"), Number(2))

# # print(distinct_variables(f_expression))

# f_expression = Product(
#     Product(Number(2), Variable("x")), Power(Variable("y"), Number(3))
# )
# print(f_expression._python_expr())
# print(distinct_variables(f_expression))
# print(f_expression.evaluate(x=3, y=2))

# 计算表达式 f(x) = (1 + math.e ** -x) ** (-1) 的值
sig_moid_expression = Power(
    Sum(Number(1), Power(Number(math.e), Negative(Variable("x")))), Number(-1)
)


def seg_moid(x):
    return (1 + math.e ** (-x)) ** (-1)


def plot_sig_moid():
    x_sets = np.linspace(-2, 2, 100)
    plt.figure(figsize=(10, 6))
    # 绘制seg_moid函数计算的值
    plt.plot(
        x_sets,
        [seg_moid(x=x_set) for x_set in x_sets],
        label="Sigmoid Function",
        color="blue",
        linewidth=2.5,
    )
    # 绘制表达式计算的值
    plt.plot(
        x_sets,
        [sig_moid_expression.evaluate(x=x_set) for x_set in x_sets],
        label="Sigmoid Expression",
        color="red",
        linewidth=0.5,
    )
    plt.title("Sigmoid Function Visualization", fontsize=14, fontweight="bold")
    plt.xlabel("Input (x)", fontsize=12)
    plt.ylabel("Output S(x)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.show()


plot_sig_moid()
