def get_formatted_name(first, last, middle=''):
    """格式化姓名"""

    if middle:
        full_name = f"{first.title()} {middle.title()} {last.title()}"
    else:
        full_name = f"{first.title()} {last.title()}"
    return full_name