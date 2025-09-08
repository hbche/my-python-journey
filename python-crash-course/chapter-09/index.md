# 第 9 章 类

## 9.1 创建和使用类

### 9.1.1 创建和使用类

```python
# 声明 Dog 类
class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令是打滚"""
        print(f"{self.name.title()} rolled over!")
```

#### **init**() 方法

类中的函数称为 **方法**。`__init__()` 方法是一个特殊方法，每当我们根据 Dog 类创
建新实例时，Python 都会自动运行它。在这个方法的名称中，开头和结尾各有两个下划线
，这是一种约定，旨在避免 Python 默认方法与普通方法发生名称冲突。务必确保
`__init()__` 方法两侧都有两个下划线，否则当我们使用类创建实例时，将不会自动调用
这个方法，进而引发难以发现的错误。

在 `__init__()` 方法中，self 参数必不可少，而且必须唯一其他形参的前面。因为当
Python 调用这个方法创建 Dog 实例时，将自动传入实参 self，该实参是一个指向实例本
身的引用，让实例能够方位类中的属性和方法。

### 9.1.2 根据类创建实例

```python
# 创建一个Dog实例，并访问该实例的属性
my_dog = Dog('Willie', 4)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")
```

#### 1. 访问属性

要访问实例的属性，可使用点号。

```python
my_dog.name
```

#### 2. 调用方法

根据 Dog 类创建实例后，就能使用点号来调用 Dog 类中定义的任何方法了。

```python
# 创建一个Dog实例，并调用实例的方法
my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
```

要调用示例的方法，需要指定示例名和想调用的方法名，并用句点连接。在遇到代码
`my_dog.sit()` 时，Python 在类 Dog 中查找方法 `sit()` 并运行其代码。

#### 3.创建多个实例

可按需根据类创建任意数量的实例。

```python
# 创建一个Dog实例，并访问该实例的属性
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
# 调用示例的方法
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
your_dog = Dog('Lucy', 3)
print(f"Your dog's name is {your_dog.name.title}.")
print(f"Your dog is {your_dog.age} years old.")
# 调用示例的方法
your_dog.sit()
your_dog.roll_over()
```

## 9.2 使用类和实例

### 9.2.1 Car 类

编写一个汽车类，存储有关汽车的信息。

```python
class Car:
    """模拟汽车类，存储汽车相关的信息"""


    def __init__(self, make, model, years):
        """初始化汽车类的信息"""
        self.make = make
        self.model = model
        self.years = years

    def get_descriptive_name(self):
        """返回格式化的描述信息"""
        long_name = f"{self.years} {self.make} {self.model}"
        return long_name.title()


# 实例化一辆汽车
my_new_car = Car('audi', 'a4', 2024)
# 打印汽车的格式化信息
print(my_new_car.get_descriptive_name())
```

### 9.2.2 给属性指定默认值

有些属性无需使用形参来定义，可在 `__init__()` 方法中为其指定默认值。

下面给汽车类增加一个参数 `odometer_reading` 显示汽车的里程数

```python
class Car:
    """模拟汽车类，存储汽车相关的信息"""


    def __init__(self, make, model, years):
        """初始化汽车类的信息"""
        self.make = make
        self.model = model
        self.years = years
        # 增加里程表读书参数，默认0
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式化的描述信息"""
        long_name = f"{self.years} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")


# 实例化一辆汽车
my_new_car = Car('audi', 'a4', 2024)
# 打印汽车的格式化信息
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

### 9.2.3 修改属性的值

可以使用三种不同的方式修改属性的值：直接通过实例修改，通过方法设置，以及通过方法
递增（增加特定的值）。

#### 1. 直接修改属性的值

```python
class Car:
--snip--

# 实例化一辆汽车
my_new_car = Car('audi', 'a4', 2024)
# 打印格式化后的描述信息
print(my_new_car.get_descriptive_name())
# 直接修改属性值
my_new_car.odometer_reading = 23
# 通过方法打印属性值
my_new_car.read_odometer()
```

#### 2. 通过方法修改属性的值

有一个能够更新属性的方法大有裨益。这样就无需直接访问属性了，而是可将值传递给方法
，由它在内部进行更新。

```python
class Car:
--snip--
    def update_odometer(self, mileage):
        """声明更新里程数的方法"""
        self.odometer_reading = mileage


# 实例化一辆汽车
my_new_car = Car('audi', 'a4', 2024)
# 打印格式化后的描述信息
print(my_new_car.get_descriptive_name())
# 通过方法修改属性值
my_new_car.update_odometer(23)
# 通过方法打印属性值
my_new_car.read_odometer()
```

#### 3. 通过方法让指定的值递增

```python
class Car:
    """模拟汽车类，存储汽车相关的信息"""


    def __init__(self, make, model, years):
        """初始化汽车类的信息"""
        self.make = make
        self.model = model
        self.years = years
        # 增加里程表读书参数，默认0
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式化的描述信息"""
        long_name = f"{self.years} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """声明更新里程数的方法"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """让里程表读数增加指定的量"""
        self.odometer_reading += miles


# 实例化一辆汽车
my_used_car = Car('subaru', 'outback', 2024)
# 打印格式化后的描述信息
print(my_used_car.get_descriptive_name())

# 通过方法修改属性值
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

# 通过方法递增属性值
my_used_car.increment_odometer(100)
# 通过方法打印属性值
my_used_car.read_odometer()
```

## 9.3 继承

在编写类时，并非总是要从头开始。如果要编写的类是一个既有的类的特殊版本，可使用继
承(inheritance)。

当一个类继承另一个类时，将自动获得后者的所有属性和方法。原有的类称为父类(parent
class)，而新类称为子类(child class)。子类不仅继承了父类的所有属性和方法，还可定
义自己的属性和方法。

### 9.3.1 子类的 `__init__()` 方法

在既有类的基础上编写新类，通常需要调用父类的 `__init__()` 方法。这将初始化在父类
的 `__init__()` 方法中定义的所有属性，从而让子类也可以使用这些属性。

```python
class Car:
    """模拟传统汽车模型"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一个句子，支出汽车的行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """更新里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles


# 声明电动轿车类
class ElectricCar(Car):
    """电动汽车的独特之处"""


    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())           # 2024 Nissan Leaf
```

`super()`是一个特殊的函数，让我们能够调用父类的方法。

### 9.3.2 给子类定义属性和方法

让一个类继承另一个类后，就可以添加区分子类和父类所需的新属性和新方法了。

```python
class Car:
    """模拟传统汽车模型"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一个句子，支出汽车的行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """更新里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles


# 声明电动轿车类
class ElectricCar(Car):
    """电动汽车的独特之处"""


    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 电车特有的属性，电池容量
        self.battery_size = 40

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")



my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())           # 2024 Nissan Leaf
my_leaf.describe_battery()
```

### 9.3.3 重写父类中的方法

在使用子类模拟的实物的行为时，如果父类中的一些方法不能满足子类的需求，就可以用下
面的办法重写：在子类中定义一个与要重写的父类方法同名的方法。这样，Python 将忽略
这个父类方法，只关注你在子类中定义的相应方法。

```python
class Car:
    """模拟传统汽车模型"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一个句子，支出汽车的行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """更新里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """加满箱油"""
        print("This car fill a gas tank!")


# 声明电动轿车类
class ElectricCar(Car):
    """电动汽车的独特之处"""


    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 电车特有的属性，电池容量
        self.battery_size = 40

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """加满箱油"""
        print("This car doesn't have a gas tank!")



my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())           # 2024 Nissan Leaf
# 调用子类特有的方法
my_leaf.describe_battery()                      # This car has a 40-kWh battery.
# 调用子类重写的方法
my_leaf.fill_gas_tank()                         # This car doesn't have a gas tank!
```

### 9.3.4 将实例用作属性

在使用代码模拟实物时，你可能会发现自己给类添加了太多细节：属性和方法越来越多，文
件越来越长。在这种情况下，可能需要将类的一部分提取出来，作为一个独立的类。将大型
类拆分成多个协同工作的小类，这种方法称为组合(composition)。

```python
class Car:
    """模拟传统汽车模型"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一个句子，支出汽车的行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """更新里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """加满箱油"""
        print("This car fill a gas tank!")


class Battery:
    """模拟电池类"""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


# 声明电动轿车类
class ElectricCar(Car):
    """电动汽车的独特之处"""


    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 电车特有的属性，电池容量
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        # print(f"This car has a {self.battery_size}-kWh battery.")
        self.battery.describe_battery()

    def fill_gas_tank(self):
        """加满箱油"""
        print("This car doesn't have a gas tank!")



my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())           # 2024 Nissan Leaf
# 调用子类特有的方法
my_leaf.describe_battery()                      # This car has a 40-kWh battery.
# 调用子类重写的方法
my_leaf.fill_gas_tank()                         # This car doesn't have a gas tank!
```
