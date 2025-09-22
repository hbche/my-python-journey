# # 练习11.1：城市和国家　编写一个函数，它接受两个形参：一个城市名和一个国家名。
# # 这个函数返回一个格式为City,Country的字符串，如Santiago, Chile。
# # 将这个函数存储在一个名为city_functions.py的模块中，并将这个文件存储在一个新的文件夹中，以免pytest在运行时，尝试运行之前编写的测试。
# # 创建一个名为test_cities.py的程序，对刚编写的函数进行测试。
# # 编写一个名为test_city_country()的函数，核实在使用类似于'santiago'和'chile'这样的值来调用该函数时，得到的字符串是正确的。
# # 运行测试，确认test_city_country()通过了。
# from city_functions import formatted_city_country

# def test_city_country():
#     result = formatted_city_country('santiago', 'chile')
#     assert result == 'Santiago, Chile'

# 练习11.2：人口数量　修改前面的函数，使其包含第三个必不可少的形参population，并返回一个格式为City, Country -population xxx的字符串，
# 如Santiago, Chile - population 5000000。
# 运行测试，确认test_city_country()未通过。
# 修改上述函数，将形参population设置为可选的。
# 再次运行测试，确认test_city_country()又通过了。

from city_functions import formatted_city_country

def test_city_country():
    result = formatted_city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'
    
# 再编写一个名为test_city_country_population()的测试，核实可以使用类似于'santiago'、'chile'和'population=5000000'这样的值来调用这个函数。
# 再次运行测试，确认test_city_country_population()通过了。

def test_city_country_population():
    result = formatted_city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile - population 5000000'