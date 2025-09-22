def smap():
    message = 'Spam'
    word = 'spam'
    for _ in range(100):
        # 循环没有局部作用域，因此在循环外部也能访问 separator
        seperator = ', '
        message += seperator + word
    message += seperator
    message += 'spam!'
    
    return message

print(message)      # NameError: name 'message' is not defined