from vector import add

# 4.1 实现translate_by函数
def translate_by(translation):
    def new_function(v):
        return add(v, translation)

    return new_function

