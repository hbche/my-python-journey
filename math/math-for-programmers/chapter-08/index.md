# 第 8 章 理解变化率

目标：

- 计算数学函数中的平均变化率
- 近似计算某点的瞬时变化率
- 绘图说明变化率本身是如何变化的
- 根据函数的变化率重建函数

## 8.1 根据体积计算平均流速

现在声明以下两个函数：

```py
def volume(t):
    return (t-4)**3 / 64 + 3.3
```

### 8.1.1 实现 average_flow_rate 函数

已知体积随时间变化的函数，我们计算指定时间内的平均流速：

$$
平均流速=\frac{体积变化量}{经过时间}
$$

对应代码如下：

```py
def average_flow_rate(v, t1, t2):
    return (v(t2)-v(t1))/(t2-t1)
```

### 8.1.2 用割线描绘平均流速

### 8.1.3 负变化率

### 8.1.4 练习

练习 8.2：实现一个 Python 函数 secant_line(f,x1,x2)，它接收函数 f(x)以及两个值
x1 和 x2，并返回一个表示随时间变化割线的新函数。例如，运行 line
=secant_line(f,x1,x2)，那么 line(3)将给出割线在 x=3 时的 y 值。

```py
def secant_line(f, x1, x2):
    """
    secant_line: 计算两点之间的割线方程

    :param f: 指定函数
    :param x1: 割线的第一个点的x坐标
    :param x2: 割线的第二个点的x坐标
    """
    def line(x):
        return (f(x2)-f(x1))/(x2-x1)*(x-x1)+f(x1)
    return line
```

练习 8.3：实现一个函数，使用上一个练习中的代码在两个给定点之间绘制函数 f 的割线
。

```py
def plot_secant(f, x1, x2, color='k'):
    line = secant_line(f, x1, x2)
    plot_function(line, x1, x2, c=color)
    plt.scatter([x1, x2], [f(x1), f(x2)], c=color)
```

## 8.2 绘制随时间变化的平均流速

```py
plot_volume(volume, 0, 10)
plot_secant(volume,1,4)
plot_secant(volume,6,8)
```

### 8.2.1 计算不同时间段的流速

```py
def interval_flow_rates(f, t1, t2, dt):
    """
    interval_flow_rates: 计算给定时间段内指定时间间隔的每一段平均速率

    :param f: 说明
    :param t1: 说明
    :param t2: 说明
    :param dt: 说明
    """
    return [
        (t, average_flow_rate(f, t, t+dt))
        for t in np.arange(t1, t2, dt)
    ]
```

### 8.2.2 绘制间隔流速图

```py
def plot_interval_flow_rates(f, t1, t2, dt):
    series = interval_flow_rates(f, t1, t2, dt)
    times, rates = [], []
    for time, rate in series:
        times.append(time)
        rates.append(rate)
    plt.scatter(times, rates)
```

## 8.2.3 练习

## 8.3 瞬时流速的近似值

### 8.3.1 计算小割线的斜率

### 8.3.2 构建瞬时流速函数

```py
def instantaneous_flow_rate(v, t, digits=6):
    """
    instantaneous_flow_rate: 以指定精度计算某个时刻的瞬时速率

    :param v: 说明
    :param t: 说明
    :param digits: 说明
    """
    tolerance = 10 ** (-digits)
    h=1
    approx = average_flow_rate(v, t-h, t+h)
    for _ in range(0, 2 * digits):
        h = h/10
        next_approx =average_flow_rate(v, t-h, t+h)
        if abs(next_approx - approx) < tolerance:
            return round(next_approx, digits)
        approx = next_approx

    raise Exception('Derivative did not converge')  # 如果超过了最大的迭代次数，就表示程序没有收敛到一个结果
```

### 8.3.3 柯里化并绘制瞬时流速函数

```py
def get_flow_rate_function(v):
    def flow_rate_function(t):
        return instantaneous_flow_rate(v, t)
    return flow_rate_function
```

绘制瞬时流速：

```py
plot_function(get_flow_rate_function(volume), 0, 10)
```

从体积函数中产生流速函数。这个过程叫做"**求导**"。

导数是一个通用程序，适用于任何足够平滑、每一个点都有切线的函数 f(x)。函数 f 的导
数写作 $f'$，所以$f'(x)$是指 f 相对于 x 的瞬时变化率。具体来说，$f'(5)$是 f(x)在
x=5 时的导数，表示当 x=5 时 f 上切线的斜率。函数的导数还有一些其他的通用表示方法
，包括：

$$
f'(x)=\frac{df}{dx}=\frac{d}{dx}f(x)
$$

当 df 和 dx 分别表示 f 和 x 的无限小变化，它们的商表示无限小割线的斜率。

## 8.4 体积变化的近似值

从已知的流速函数得到体积函数。这个过程叫做"**积分**"。

### 8.4.1 计算短时间间隔内的体积变化

$$
平均流速 = \frac{体积的变化}{经过的时间}
$$

重新调整这个公式：

$$
体积的变化 = 平均流速 \times 经过的时间
$$

```py
def small_volume_change(q, t, dt):
    """
    small_volume_change: 计算瞬时体积变化

    :param q: 瞬时流速函数
    :param t: 时刻，用于计算瞬时速率
    :param dt: 经过的时间
    """
    return q(t) * dt
```
