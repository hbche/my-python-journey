# 定义地标字典
landmarks = {
    "Yellow Crane Tower": "Wuhan Hubei",              # 黄鹤楼
    "The Bund": "Shanghai Shanghai",                 # 外滩
    "Terracotta Army": "Xi'an Shaanxi",              # 秦始皇兵马俑
    "Great Wall": "Beijing Beijing",                 # 万里长城（北京段最有代表性）
    "Forbidden City": "Beijing Beijing",             # 故宫
    "Temple of Heaven": "Beijing Beijing",           # 天坛
    "Summer Palace": "Beijing Beijing",              # 颐和园
    "West Lake": "Hangzhou Zhejiang",                # 西湖
    "Potala Palace": "Lhasa Tibet",                  # 布达拉宫
    "Mogao Caves": "Dunhuang Gansu",                 # 莫高窟
}


def lookup_landmark(landmark):
    try:
        location = landmarks[landmark]
        city, province = location.split()
    except KeyError as e:
        raise KeyError("Landmark not found.") from e
    print(f"{landmark} is in {city}, {province}")
    
lookup_landmark('Yellow Crane Tower')
lookup_landmark('Mount Tai') # 查找 泰山
lookup_landmark('Li River') # 查找 漓江