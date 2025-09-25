# 第 9 章 集合与迭代

## 9.1 循环

Python 中有两种类型的循环：while 循环和 for 循环。这并不意味着两者可以互换，相反
，每种循环都有自己独特的目的。

### 9.1.1 while 循环

while 循环是非常传统的循环。只要其标头中的表达式的计算结果为 True ，循环体就会执
行。

```python
# 演示 while 循环

number = None

while number is None:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("You must enter a number.")

print(f"You entered {number}")
```

只要 number 的值为 None ，while 循环的代码块就会一直重复。一旦用户输入一个有效的
整数，就会退出循环，并将数字输出到控制台。

如果想提供一种直接退出而不是依赖输入数字的机制，我们可以使用 break 关键字手动退
出循环。这里允许用户通过输入 q 而不是数字来退出循环：

```python
# 演示 while 循环

number = None

while number is None:
    try:
        raw = input("Enter a number: ")
        if raw == 'q':
            # 提前终止循环
            break
        number = int(raw)
    except ValueError:
        print("You must enter a number.")

print(f"You entered {number}")
```

输出如下：

```bash
Enter a number: q
You entered None
```

最后一行输出不对。我们希望程序立即退出。

为了解决这个问题，我们可以使用 else 子句。当 Python 循环正常结束时，运行 else 子
句；但是如果循环因终端、返回或引发的异常而终止，则 else 子句不会运行。

```python
# 演示 while 循环

number = None

while number is None:
    try:
        raw = input("Enter a number: ")
        if raw == 'q':
            # 提前终止循环
            break
        number = int(raw)
    except ValueError:
        print("You must enter a number.")
else:
    # 循环顺利结束时才执行，任何提前结束的场景都不执行else子句
    print(f"You entered {number}")
```

### 9.1.2 for 循环

和 while 循环一样，for 循环也有一个 else 子句，这个 else 子句仅在循环正常结束时
运行，当循环因中断、返回或引发的异常而提前终止时则不会运行。

```python
# 演示 for 循环遍历一组值
numbers = ["One", "Two", "Three"]

for number in numbers:
    print(number)
else:
    print("We're done!")
```

## 9.2 集合

集合是一种容器，其中包含以某种方式组织的一项或多项。每一项都被绑定到一个值，值本
身不包含在集合中。Python 中有 5 种基本的集合：元组、列表、双端队列、可变集合和字
典。每种集合都有多种变体。

### 9.2.1 元组

元组（tuple）是一个不可变序列（类似数组的集合）​，这意味着元组一旦被创建，其中的
元素就不能被添加、删除或重新排序。

通常，元组用于存储异构类型的顺序排列的数据，例如，当需要将类型不同但相互关联的值
放在一起时。下面将一个包含客户名称、咖啡订单和订单大小的元组。

```python
order = ("Jason", "pumkin spice latte", 12)
```
