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

在 `__init__()` 方法中，**self** 参数必不可少，而且必须位于其他形参的前面。因为
当 Python 调用这个方法创建 Dog 实例时，将自动传入实参 self，该实参是一个指向实例
本身的引用，让实例能够方位类中的属性和方法。

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

要调用实例的方法，需要指定实例名和想调用的方法名，并用句点连接。在遇到代码
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

有一个能够更新属性的方法大有裨益。这样就无需直接访问属性了，而是将值传递给方法，
由它在内部进行更新。

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
这个父类方法，只关注我们在子类中定义的相应方法。

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

在使用代码模拟实物时，我们可能会发现自己给类添加了太多细节：属性和方法越来越多，
文件越来越长。在这种情况下，可能需要将类的一部分提取出来，作为一个独立的类。将大
型类拆分成多个协同工作的小类，这种方法称为组合(composition)。

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

### 9.3.5 模拟实物

在解决上述问题时，从较高的逻辑层面（而不是语法层面）思考。我们考虑的不是
Python，而是如何使用代码来表示实际事物。达到这种境界后，我们会经常发现，对现实世
界的建模方法没有对错之分。有些方法的效率更高，但要找出效率最高的表示法，需要一定
的实践。只要代码能够像我们希望的那样运行，就说明我们已经做得很好了！即便发现自己
不得不多次尝试使用不同的方法来重写类，也不必气馁。要编写出高效、准确的代码，这是
必经之路。

## 9.4 导入类

随着不断地给类添加功能，文件可能变得很长，即便妥善地使用了继承和组合亦如此。遵循
Python 的整体理念，应该让文件尽量整洁。Python 在这方面提供了帮助，允许我们将类存
储在模块中，然后在主程序中导入所需的模块。

### 9.4.1 导入单个类

在 car.py 模块中定义 Car 类：

```python
class Car:
    """模拟传统油车模型"""


    def __init__(self, make, model, years):
        """初始化汽车类的信息"""
        self.make = make
        self.model = model
        self.years = years
        # 增加里程表读书参数，默认0
        self.odometer_reading = 0
        # 增加油箱容量，默认值为15
        self.fuel_tank_capacity = 15

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

    def fill_gas_tank(self):
        """打印一条加满油箱的消息"""
        print(f"This car's gas tank capacity is {self.fuel_tank_capacity} gallons.")
```

在 my_car.py 文件中导入 car 模块：

```python
from car_module import Car
# 实例化一辆汽车
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.fill_gas_tank()
my_new_car.read_odometer()
my_new_car.update_odometer(500)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
```

### 9.4.2 在同一个模块中存储多个类

尽管同一个模块中的类之间应该存在某种相关性，但其实可以根据需要在一个模块中存储任
意数量的类。

```python car.py
class Car:
    """模拟传统油车模型"""


    def __init__(self, make, model, years):
        """初始化汽车类的信息"""
        self.make = make
        self.model = model
        self.years = years
        # 增加里程表读书参数，默认0
        self.odometer_reading = 0
        # 增加油箱容量，默认值为15
        self.fuel_tank_capacity = 15

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

    def fill_gas_tank(self):
        """打印一条加满油箱的消息"""
        print(f"This car's gas tank capacity is {self.fuel_tank_capacity} gallons.")

class Battery:
    """模拟电动汽车的电瓶"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go approximately {range} miles on a full charge.")

class ElectricCar(Car):
    """模拟电动汽车的独特之处"""

    def __init__(self, make, model, years):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, years)
        self.battery = Battery()

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
```

在 my_car.py 文件中导入 car 模块：

```python
from car_module import ElectricCar
# 实例化一辆电动汽车
my_tesla = ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

### 9.4.3 从一个模块中导入多个类

可以根据需要在程序文件中导入任意数量的类。

```python
from car_module import ElectricCar, Car
my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

# 实例化一辆电动汽车
my_tesla = ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())
```

### 9.4.4 导入整个模块

还可以先导入整个模块，再使用点号访问需要的类。这种导入方法很简单，代码也易读。由
于创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突。

```python
import car_module as car
my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())
```

### 9.4.5 导入模块中的所有类

要导入模块中的每个类，可使用下面的语法：

```python
from module_name import *
```

```python
from car_module import *

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())
```

### 9.4.6 在一个模块中导入另一个模块

有时候，需要将类分散到多个模块中，以免模块太大或者在同一个模块中存储不相关的类。
在将类存储在多个模块中时，我们可能会发现一个模块中的类依赖于另一个模块中的类。在
这种情况下，可在前一个模块中导入必要的类。

```python
from car_module import Car

class Battery:
    """模拟电动汽车的电瓶"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go approximately {range} miles on a full charge.")

class ElectricCar(Car):
    """模拟电动汽车的独特之处"""

    def __init__(self, make, model, years):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, years)
        self.battery = Battery()

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
```

```python
from car_module import Car
from electric_car_module import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())
```

### 9.4.7 使用别名

假设要在程序中创建大量电动汽车实例，需要反复输入 ElectricCar，非常烦琐。为了避免
这种烦恼，可在 import 语句中给 ElectricCar 指定一个别名：

```python
from electric_car_module import ElectricCar as EC

my_tesla = EC('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())
```

### 9.4.8 找到合适的工作流程

一开始应让代码结构尽量简单。首先尝试在一个文件中完成所有的工作，确定一切都能正确
运行后，再将类移到独立的模块中。如果我们喜欢模块和文件的交互方式，可在项目开始时
就尝试将类存储到模块中。先找出让我们能够编写出可行代码的方式，再尝试让代码更加整
洁。

## 9.5 Python 标准库

Python 标准库是一组模块，在安装 Python 时已经包含在内。我们现在已经对函数和类的
工作原理有了大致的了解，可以开始使用其他程序员编写好的模块了。我们可以使用标准库
中的任何函数和类，只需在程序开头添加一条简单的 import 语句即可。下面来看看模块
random，它在我们模拟很多现实情况时很有用。

#### 9.5.1 randint 函数

```python
from random import randint

# 生成指定范围内的整数，包含范围的起点和终点
rand_int_num = randint(1, 6)
print(rand_int_num)
```

### 9.5.2 choice 函数

```python
choice_list = ['apple', 'banana', 'orange', 'pear']
# 从列表中随机选择一个元素
rand_choice = choice(choice_list)
print(rand_choice)
```

## 9.6 类的编程风格

1. 类名应采用**驼峰命名法**，即将类名中的每个单词的首字母都大写，并且不使用下划
   线。实例名和模块名都采用全小写格式，并在单词之间加上下划线。

2. 对于每个类，都应在类定义后面紧跟一个文档字符串。这种文档字符串简要地描述类的
   功能，我们应该遵循编写函数的文档字符串时采用的格式约定。每个模块也都应包含一
   个文档字符串，对其中的类可用来做什么进行描述。

3. 可以使用空行来组织代码，但不宜过多。在类中，可以使用一个空行来分隔方法；而在
   模块中，可以使用两个空行来分隔类。

4. 当需要同时导入标准库中的模块和我们编写的模块时，先编写导入标准库模块的 import
   语句，再添加一个空行，然后编写导入我们自己编写的模块的 import 语句。在包含多
   条 import 语句的程序中，这种做法让人更容易明白程序使用的各个模块来自哪里。

## 9.7 小结

1. 学习类声明
2. 学习`__init__()`方法
3. 学习声明类属性、默认属性、类方法
4. 学习类继承、学习`super()`方法调用父类方法
5. 学习子类扩展方法、重写父类中的方法
6. 学习在模块中声明类、在其他模块中导入类
7. 学习使用标准库 random 模块中的 randint 和 choice 函数
8. 学习类编程规范
