from math import sin, cos, pi

def z(t, speed=20, theta=45):
    """
    z: 滞空时间与垂直高度之间的函数
    
    :param t: 说明
    :param speed: 说明
    :param theta: 说明
    """
    return speed * sin(theta * pi / 180) * t + ((-9.81) * t **2 )/2

def r(theta, speed=20):
    """
    r: 射程与发射角度之间的函数
    
    :param speed: 发射速度
    :param theta: 发射角度
    """

    return (-2 * speed * speed / -9.81) * sin(theta * pi / 180) * cos(theta * pi / 180) 