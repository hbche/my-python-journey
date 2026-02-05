import math
from abc import ABC, abstractmethod

_function_python = {
    "sin": "math.sin({})",
    "cos": "math.cos({})",
    "ln": "math.log({})",
    "log": "math.log({})",
    "sqrt": "math.sqrt({})",
}

_function_bindings = {
    "sin": math.sin,
    "cos": math.cos,
    "ln": lambda x: math.log(x, math.e),
    "log": math.log,
}


class Expression(ABC):
    @abstractmethod
    def _python_expr() -> str:
        """
        _python_expr: 用于获取表达式对应的字符串形式
        """
        pass

    def python_function(self, **bindings):
        # 指定eval的全局作用域
        global_vars = {"math": math}
        # 通过eval执行字符串对应的python代码
        return eval(self._python_expr(), global_vars, bindings)

    @abstractmethod
    def evaluate(self, **bindings):
        """
        evaluate: 根据传入的参数计算表达式的值
        """
        pass

    @abstractmethod
    def expand(self):
        """
        expand: 计算展开的表达式
        """
        pass


class Number(Expression):
    """
    Number: 表示数字的表达式
    """

    def __init__(self, number):
        self.number = number

    def _python_expr(self):
        return f"{self.number}"

    def evaluate(self, **bindings):
        return self.number

    def expand(self):
        """
        如果是变量或数字，已经是一个独立的单元，无法再继续展开了
        """
        return self


class Variable(Expression):
    """
    Variable: 表示变量的表达式
    """

    def __init__(self, symbol: str):
        self.symbol = symbol

    def _python_expr(self):
        return f"{self.symbol}"

    def evaluate(self, **bindings):
        try:
            return bindings[self.symbol]
        except:
            raise KeyError(f"Variable '{self.symbol}' is not bound.")

    def expand(self):
        """
        如果是变量或数字，已经是一个独立的单元，无法再继续展开了
        """
        return self


class Sum(Expression):
    """
    Sum: 加法表达式
    """

    def __init__(self, *exps):  # 允许计算任意个项的和，从而可以将两个或更多表达式相加
        self.exps = exps

    def _python_expr(self):
        return f"({'+'.join(f'{exp._python_expr()}' for exp in self.exps)})"

    def evaluate(self, **bindings):
        return sum(exp.evaluate(**bindings) for exp in self.exps)

    def expand(self):
        """
        加法运算，需要递归计算每个表达式的展开表达式
        """
        return Sum(*[exp.expand() for exp in self.exps])


class Difference(Expression):
    """
    Difference: 减法表达式
    """

    def __init__(self, exp1: Expression, exp2: Expression):
        self.exp1 = exp1  # 被减数
        self.exp2 = exp2  # 减数

    def _python_expr(self):
        return f"({self.exp1._python_expr()} - {self.exp2._python_expr()})"

    def evaluate(self, **bindings):
        return self.exp1.evaluate(**bindings) - self.exp2.evaluate(**bindings)

    def expand(self):
        return Difference(self.exp1.expand(), self.exp2.expand())


class Product(Expression):
    """
    Product: 乘法表达式
    """

    def __init__(self, exp1: Expression, exp2: Expression):
        self.exp1 = exp1
        self.exp2 = exp2

    def _python_expr(self):
        return f"({self.exp1._python_expr()} * {self.exp2._python_expr()})"

    def evaluate(self, **bindings):
        return self.exp1.evaluate(**bindings) * self.exp2.evaluate(**bindings)

    # TODO
    # def expand(self):
    # expanded1 = self.exp1.expand()
    # expanded2 = self.exp2.expand()

    # if isinstance(expanded1, Sum):  # 如果乘积的第一项是求和，则使用分配率进行展开
    #     return Sum(expanded1.expand())


class Quotient(Expression):
    """
    Quotient: 除法表达式
    """

    def __init__(self, numerator: Expression, denominator: Expression):
        self.numerator = numerator  # 分子
        self.denominator = denominator  # 分母

    def _python_expr(self):
        return f"({self.numerator._python_expr()} / {self.denominator._python_expr()})"

    def evaluate(self, **bindings):
        return self.numerator.evaluate(**bindings) / self.denominator.evaluate(
            **bindings
        )


class Negative(Expression):
    """
    Negative: 取反表达式
    """

    def __init__(self, exp: Expression):
        self.exp = exp

    def _python_expr(self):
        return f"(-{self.exp._python_expr()})"

    def evaluate(self, **bindings):
        return -self.exp.evaluate(**bindings)


class Power(Expression):
    """
    Power: 幂函数表达式
    """

    def __init__(self, base: Expression, exponent: Expression):
        self.base = base
        self.exponent = exponent

    def _python_expr(self):
        return f"({self.base._python_expr()}**{self.exponent._python_expr()})"

    def evaluate(self, **bindings):
        return self.base.evaluate(**bindings) ** (self.exponent.evaluate(**bindings))


class Function:
    """
    Function: 使用字符串保存函数名称
    """

    def __init__(self, name):
        self.name = name


class Apply(Expression):
    """
    Apply: 存储一个函数以及传入该函数的参数
    """

    def __init__(self, function: Function, argument: Expression):
        self.funciton = function
        self.argument = argument

    def _python_expr(self):
        return _function_python[self.funciton.name].format(self.argument._python_expr())

    def evaluate(self, **bindings):
        return _function_bindings[self.funciton.name](
            self.argument.evaluate(**bindings)
        )


def distinct_variables(exp: Expression):
    """
    distinct_variables: 根据函数表达式的组合结构，获取函数表达式中的变量列表

    :param exp: 说明
    :type exp: Expression
    """
    if isinstance(exp, Variable):
        return set(exp.symbol)
    elif isinstance(exp, Number):
        return set()
    elif isinstance(exp, Sum):
        return set().union(*[distinct_variables(exp_item) for exp_item in exp.exps])
    elif isinstance(exp, Difference):
        return distinct_variables(exp.exp1).union(distinct_variables(exp.exp2))
    elif isinstance(exp, Product):
        return distinct_variables(exp.exp1).union(distinct_variables(exp.exp2))
    elif isinstance(exp, Quotient):
        return distinct_variables(exp.numerator).union(
            distinct_variables(exp.denominator)
        )
    elif isinstance(exp, Power):
        return distinct_variables(exp.base).union(distinct_variables(exp.exponent))
    elif isinstance(exp, Negative):
        return distinct_variables(exp.exp)
    elif isinstance(exp, Apply):
        return set(distinct_variables(exp.argument))
    elif isinstance(exp, Function):
        return set()
    else:
        raise TypeError("Not a valid expression.")
