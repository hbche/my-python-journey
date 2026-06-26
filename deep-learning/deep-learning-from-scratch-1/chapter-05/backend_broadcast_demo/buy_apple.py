from layer_naive import MulLayer


def buy_apple():
    # 苹果个数
    apple_total = 2
    # 苹果单价
    apple_price = 100
    # 税率
    tax = 1.1

    # 苹果计算的乘法层
    apple_mul_layer = MulLayer()
    # 总价计算的乘法层
    tax_mul_layer = MulLayer()

    # 利用乘法层计算总价
    total_price = tax_mul_layer.forward(
        apple_mul_layer.forward(apple_price, apple_total), tax
    )
    print(f"Total price is {total_price}")
    # Total price is 220.00000000000003
    # 根据乘法层的反向传播计算各个参数的导数
    delta_out = 1
    # 计算苹果总价和税率的导数
    delta_apple_total_priace, delta_tax = tax_mul_layer.backward(delta_out)
    print(f"Delta tax is {delta_tax}")
    # Delta tax is 200
    # 根据苹果总价的导数再结合乘法层的反向传播计算苹果单价和苹果个数的导数
    delta_apple_price, delta_apple_total = apple_mul_layer.backward(
        delta_apple_total_priace
    )
    print(
        f"Delta apple price is {delta_apple_price}, delta apple total is {delta_apple_total}"
    )
    # Delta apple price is 2.2, delta apple total is 110.00000000000001


if __name__ == "__main__":
    buy_apple()
