# 从文件夹中读取数据并计算平均值，演示 finally 子句

def average_file(path):
    file = open(path, 'r')
    
    try:
        numbers = [float(n) for n in file.readlines()]
    # except FileNotFoundError:
    except ValueError as e:
        # 防止文件中存在非数值类型的字符
        raise ValueError("File contains non-numberic values.") from e
    else:
        try:
            return sum(numbers) / len(numbers)
        except ZeroDivisionError as e:
            # 防止文件为空，导致分母为0
            raise ValueError("Empty file.") from e
    finally:
        print("Closing file.")
        file.close()
        
# print(average_file('numbers_good.txt'))
# print(average_file('numbers_bad.txt'))
# print(average_file('numbers_empty.txt'))
print(average_file('nonexistent.txt'))