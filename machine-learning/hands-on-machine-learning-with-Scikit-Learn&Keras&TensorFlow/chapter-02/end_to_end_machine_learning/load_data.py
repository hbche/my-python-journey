import tarfile
import urllib.request
from pathlib import Path

import pandas as pd


def load_housing_data():
    """
    获取房屋数据集
    """
    tarball_path = Path("datasets/housing.tgz")
    # 如果本地datasets文件夹下没有没有housing.tgz压缩包，则会从github请求
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        # urlretrieve是urllib模块的一个核心函数，专门用于从指定的URL地址下载文件并直接保存到本地文件系统。
        urllib.request.urlretrieve(url, tarball_path)
    with tarfile.open(tarball_path) as housing_tarball:
        # extractall方法新增了一个filter参数，用于指定提取策略
        # data 过滤器会忽略许多UNIX文件系统/归档格式的专有特性，适合纯粹的数据提取场景
        # tar 过滤器模拟GUN tar 行为，保留更多类UNIX的系统特性
        # full_trusted过滤器是完全信任归档文件
        # 我们此处只为提取数据，所以只需要使用 data 过滤器即可
        housing_tarball.extractall(path="datasets", filter="data")
        # 使用pandas读取csv文件，返回DataFrame结构
    return pd.read_csv(Path("datasets/housing/housing.csv"))
