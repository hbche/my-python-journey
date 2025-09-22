from name_functions import get_formatted_name

def test_first_last_name():
    """测试get_formatted_name"""

    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_middle_last_name():
    """测试get_formatted_name包含中间名的场景"""

    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'