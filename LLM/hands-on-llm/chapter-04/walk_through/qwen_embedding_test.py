# https://docs.langchain.com/oss/python/integrations/embeddings/dashscope
import os

import numpy as np
from dotenv import find_dotenv, load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv(find_dotenv())

embeddings = DashScopeEmbeddings(
    model="text-embedding-v4", dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
)

query_list = [
    "机器学习",
    "深度学习",
    "强化学习",
    "大语言模型",
    "南瓜",
]

embedding_list = [np.array(embeddings.embed_query(query)) for query in query_list]

# for embbeding_item in embedding_list:
#     print(embbeding_item)

# print(
#     f"{query_list[0]} 生成长度为 {len(embedding_list[0])} 的 embedding，其前 30 个值为：{embedding_list[0][0:30]}"
# )

# for i in range(0, len(query_list) - 1):
#     for j in range(i + 1, len(query_list)):
#         print(
#             f'"{query_list[i]}" 与 "{query_list[j]}" 的点积为：{np.dot(embedding_list[i], embedding_list[j])}'
#         )
# # "机器学习" 与 "深度学习" 的点积为：0.8275871562915844
# # "机器学习" 与 "强化学习" 的点积为：0.6015957698292973
# # "机器学习" 与 "大语言模型" 的点积为：0.4871444086361928
# # "机器学习" 与 "南瓜" 的点积为：0.2838396135901741
# # "深度学习" 与 "强化学习" 的点积为：0.6374841367136348
# # "深度学习" 与 "大语言模型" 的点积为：0.5706876848085725
# # "深度学习" 与 "南瓜" 的点积为：0.2797307143636383
# # "强化学习" 与 "大语言模型" 的点积为：0.4921765930753128
# # "强化学习" 与 "南瓜" 的点积为：0.23933468900412888
# # "大语言模型" 与 "南瓜" 的点积为：0.21115782572566394

for i in range(0, len(query_list) - 1):
    for j in range(i + 1, len(query_list)):
        print(
            f'"{query_list[i]}" 与 "{query_list[j]}" 的余弦相似度为：{cosine_similarity(embedding_list[i].reshape(1, -1), embedding_list[j].reshape(1, -1))}'
        )
# "机器学习" 与 "深度学习" 的余弦相似度为：[[0.8275872]]
# "机器学习" 与 "强化学习" 的余弦相似度为：[[0.60159578]]
# "机器学习" 与 "大语言模型" 的余弦相似度为：[[0.48714443]]
# "机器学习" 与 "南瓜" 的余弦相似度为：[[0.28383964]]
# "深度学习" 与 "强化学习" 的余弦相似度为：[[0.63748416]]
# "深度学习" 与 "大语言模型" 的余弦相似度为：[[0.57068772]]
# "深度学习" 与 "南瓜" 的余弦相似度为：[[0.27973075]]
# "强化学习" 与 "大语言模型" 的余弦相似度为：[[0.4921766]]
# "强化学习" 与 "南瓜" 的余弦相似度为：[[0.23933471]]
# "大语言模型" 与 "南瓜" 的余弦相似度为：[[0.21115785]]