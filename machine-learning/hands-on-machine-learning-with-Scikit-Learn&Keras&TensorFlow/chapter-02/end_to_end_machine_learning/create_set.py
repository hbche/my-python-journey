import numpy as np
import pandas as pd
from zlib import crc32


def shuffle_and_split_data(data: pd.DataFrame, test_ratio: float):
    """
    清洗数据并分出训练集和测试集
    """
    # 根据data生成与其索引对应的随机索引列表
    shuffle_indices = np.random.permutation(len(data))
    # 计算测试集的大小
    test_set_size = int(len(data) * test_ratio)
    # 计算测试集对应的索引列表
    test_indices = shuffle_indices[:test_set_size]
    # 计算训练集对应的索引列表
    train_indices = shuffle_indices[test_set_size:]
    # 获取训练集数据和测试集数据
    # 切记：DataFrame.iloc不是方法
    return data.iloc[train_indices], data.iloc[test_indices]


def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier) < test_ratio * 2 ** 32)


def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[-in_test_set], data.loc[in_test_set]