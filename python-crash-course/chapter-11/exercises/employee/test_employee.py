# # 测试类

# from employee import Employee

# def test_give_default_raise():
#     employee = Employee('Robin', 'Green', 20000)
#     employee.give_raise()
#     assert employee.annual_salary == 25000
    

# def test_give_custom_raise():
#     employee = Employee('Robin', 'Green', 20000)
#     employee.give_raise(4000)
#     assert employee.annual_salary == 24000

# 使用夹具测试类
from employee import Employee
import pytest

@pytest.fixture
def custom_employee():
    employee = Employee('Robin', 'Green', 20000)
    return employee

def test_give_default_raise(custom_employee):
    custom_employee.give_raise()
    assert custom_employee.annual_salary == 25000
    

def test_give_custom_raise(custom_employee):
    custom_employee.give_raise(4000)
    assert custom_employee.annual_salary == 24000