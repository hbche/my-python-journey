# 演示使用日志保存异常信息
import logging
from operator import add, sub, mul, truediv
import sys

# 设置日志级别和日志文件
logging.basicConfig(filename="log.txt", level=logging.INFO)

def calculator(a, b, op):
    """进行加减乘除的算数计算"""
    a = float(a)
    b = float(b)
    match op:
        case '+':
            return add(a, b)
        case '-':
            return sub(a, b)
        case '*':
            return mul(a, b)
        case '/':
            return truediv(a, b)
        # 其余未支持的运算符将主动抛出一个 NotImplementedError 的错误
        case _:
            raise NotImplementedError(f"No operator {op}")

print("""CALCULATOR
      Use postfix notation
      Ctrl+C or Ctrl+D to quit.""")

while True:
    try:
        equation = input(" ").split()
        result = calculator(*equation)
        print(result)
    except NotImplementedError as e:
        # 如果输入了一个除 + - * / 之外的操作符，将引发 NotImplementedError
        print(f"<!> Invalid operator.")
        logging.info(e)
    except ValueError as e:
        # 当输入非数字的字符，float转换将引发 ValueError
        print(f"<!> Expected format: <A> <B> <OP>")
        logging.info(e)
    except TypeError as e:
        # 如果向函数传递了太多或太少的参数，将引发 TypeError
        print(f"<!> Wrong number of arguments. Use: <A> <B> <OP>.")
        logging.info(e)
    except ZeroDivisionError as e:
        # 如果进行除法运算的第二个参数为0，将引发 ZeroDivisionError
        print(f"<!> Cannot divide by zero.")
        logging.info(e)
    except Exception as e:
        logging.exception(e)
        raise