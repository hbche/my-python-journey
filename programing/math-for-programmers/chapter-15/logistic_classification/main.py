import matplotlib.pyplot as plt
from car_data import Car, bmws, priuses
from plot_data import plot_data

all_car_data = []
all_bmws = []
all_priuses = []
for bmw in bmws:
    all_car_data.append((bmw.mileage, bmw.price, 1))
    all_bmws.append((bmw.mileage, bmw.price, 1))
for prius in priuses:
    all_car_data.append((prius.mileage, prius.price, 0))
    all_priuses.append((prius.mileage, prius.price, 0))


def bmw_finder(price):
    """
    基于价格特征对车辆进行分类，当价格大于25000时，认为是宝马
    """
    if price > 20000:
        return 1
    else:
        return 0


def test_classifier(f, data: tuple[Car]):
    """
    测试分类器的准确率
    """
    trues = 0
    falses = 0
    for mileage, price, is_bmw in data:
        if bmw_finder(price) == is_bmw:
            trues += 1
        else:
            falses += 1

    return trues / (trues + falses)


# print(test_classifier(bmw_finder, all_car_data))  # 0.735

plot_data(all_bmws)
plot_data(all_priuses)

plt.show()
