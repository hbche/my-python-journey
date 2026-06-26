from layer_naive import AddLayer, MulLayer

# 以买苹果和买橘子的案例测试加法层和乘法层的实现


def buy_apple_orange():
    apple_price = 100
    apple_count = 2
    orange_price = 150
    orange_count = 3
    tax = 1.1

    apple_mul_layer = MulLayer()
    orange_mul_layer = MulLayer()
    add_layer = AddLayer()
    tax_mul_layer = MulLayer()

    # 计算苹果总价
    apple_total_price = apple_mul_layer.forward(apple_price, apple_count)
    # 橘子苹果总价
    orange_total_price = orange_mul_layer.forward(orange_price, orange_count)
    # 计算苹果和橘子的总价
    total_price = add_layer.forward(apple_total_price, orange_total_price)
    # 计算税后的总价
    tax_total_price = tax_mul_layer.forward(total_price, tax)
    print(
        f"苹果单价为{apple_price}， 橘子单价为{orange_price}，税率是10%， 现在购买{apple_count}个苹果和{orange_count}个橘子，税后总价为：{tax_total_price}"
    )
    # 苹果单价为100， 橘子单价为150，税率是10%， 现在购买2个苹果和3个橘子，税后总价为：715.0000000000001

    # 反向传播计算导数
    # 计算税率的导数
    dout = 1
    dout_price, dout_tax = tax_mul_layer.backward(dout)
    print(f"汇率的导数为 {dout_tax}")
    # 汇率的导数为 650
    print(f"水果税前总价的导数为 {dout_price}")
    # 水果税前总价的导数为 1.1
    dout_apple_total_price, dout_orange_total_price = add_layer.backward(dout_price)
    dout_apple_price, dout_apple_count = apple_mul_layer.backward(
        dout_apple_total_price
    )
    print(f"苹果单价的导数为 {dout_apple_price}，苹果个数的导数为 {dout_apple_count}")
    # 苹果单价的导数为 2.2，苹果个数的导数为 110.00000000000001
    dout_orange_price, dout_orange_count = orange_mul_layer.backward(
        dout_orange_total_price
    )
    print(f"橘子单价的导数为 {dout_orange_price}，橘子个数的导数为 {dout_orange_count}")
    # 橘子单价的导数为 3.3000000000000003，橘子个数的导数为 165.0


if __name__ == "__main__":
    buy_apple_orange()
