# 数据库搭建

## 知识库文档处理

### 知识库设计

我们可以通过 langchain 的各种 Loader 对我们的知识文档进行加载解析，我们将我们的知识文档放在 "../../data_base/konwledge_db" 目录下。

### 文档加载

新版本 langchain 中 loader 被拆分到 langchain-community 中去了。

#### PDF 文档

安装依赖：

```bash
pip install langchain-community pymupdf
```

实现代码如下：

```py
from langchain_community.document_loaders import PyMuPDFLoader

# 创建一个 PyMuPDFLoader 实例，输入为待加载的 pdf 文档路径
loader = PyMuPDFLoader(".\\data_base\\konwledge_db\\pumpkin_book.pdf")

# 调用 PyMuPDFLoader 的load方法对 pdf 文件进行加载
pages = loader.load()
```

##### 探索加载的数据

`page` 变量的类型为 `List`，`page` 中的每一个元素为一个文档，变量类型为 `langchain.schema.document.Document`，文档变量类型包含两个属性：

- `page_content` 包含该文档的内容
- `metadata` 为文档相关的描述性数据

```py
page = pages[1]
print(f"文档的类型为：\n{type(page)}")
print(f"第一页文档的描述信息为：\n{page.metadata}")
print(f"第一页文档的内容为：\n{page.page_content[0:1000]}")
```

#### MD 文档

安装依赖：

```bash
pip install "unstructured[all-docs]" -i https://pypi.tuna.tsinghua.edu.cn/simple
```

示例代码：

```py
"""加载 Markdown 文档并打印信息"""
from pathlib import Path

from langchain_community.document_loaders import UnstructuredMarkdownLoader

# 使用脚本所在目录的绝对路径
script_dir = Path(__file__).parent
file_path = script_dir / "data_base" / "konwledge_db" / "1.Introduction.md"

loader = UnstructuredMarkdownLoader(str(file_path))
pages = loader.load()

print(f"每一个文档的类型：{type(pages[0])}\n")
print(f"文档的描述信息：\n{pages[0].metadata}")
print(f"文档的内容：\n{pages[0].page_content}")
```

### 文档分隔

Langchain 中文本分割器都根据 `chunk_size` (块大小)和 `chunk_overlap` (块与块之间的重叠大小)进行分割。

- `chunk_size`: 指每个块包含的字符或 Token （如单词、句子等）的数量
- `chunk_overlap`: 指两个块之间共享的字符数量，用于保持上下文的连贯性，避免分割丢失上下文信息

Langchain 提供多种文档分割方式，区别在怎么确定块与块之间的边界、块由哪些字符/token组成、以及如何测量块大小

- `RecursiveCharacterTextSplitter()`: 按字符串分割文本，递归地尝试按不同的分隔符进行分割文本
- `CharacterTextSplitter()`: 按字符来分割文本
- `MarkdownHeaderTextSplitter()`: 基于指定的标题来分割 markdown 文档
- `TokenTextSplitter()`: 按token来分割文
- `SentenceTransformersTokenTextSplitter()`: 按token来分割文本
- `Language()`: 用于 CPP、Python、Ruby、Markdown 等
- `NLTKTextSplitter()`: 使用 NLTK（自然语言工具包）按句子分割文本
- `SpacyTextSplitter()`: 使用 Spacy按句子的切割文本
- ...

示例代码：

```py
from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 指定知识库中单段文本长度
CHUNK_SIZE = 500
# 指定知识库中相邻文本重合长度
OVERLAP_SIZE = 50

script_dir = Path(__file__).parent
file_path = script_dir / ".." / ".." / "data_base" / "konwledge_db" / "pumpkin_book.pdf"
# 此处以 pdf 为例
loader = PyMuPDFLoader(str(file_path))
pages = loader.load()
page = pages[1]

# 使用递归字符文本分割器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE, chunk_overlap=OVERLAP_SIZE
)
# # 针对单页文本进行分割
# sliptted_text = text_splitter.split_text(page.page_content[0:1000])
# print(sliptted_text)

# 针对文档进行分割
split_docs = text_splitter.split_documents(pages)
print(f"切割后的文件数量：{len(split_docs)}")

print(
    f"切分后的字符数（可以用来大致评估 Token 数）：{sum([len(doc.page_content) for doc in split_docs])}"
)
```

### 文档词向量化

在机器学习和自然语言处理（NLP）中，Embeddings（嵌入）是一种将类别数据，如单词、句子或者整个文档，转化为实数向量的技术。这些实数向量可以被计算机更好地理解和处理。嵌入背后的主要想法是，相似或相关的对象在嵌入空间中的距离应该很近。

我们可以将我们切分部分的数据进行 `Embedding` 处理。

这里提供了三种方式，一种是直接使用 openai 的模型去生成 embedding，另一种是使用 HuggingFace 上的模型去生成 embedding。

- openai 的模型需要消耗 api，对于大量的token 来说成本会比较高，但是非常方便。
- HuggingFace 的模型可以本地部署，可自定义合适的模型，可玩性较高，但对本地的资源有部分要求。
- 采取其他平台的 api。对于获取 OpenAi key 不方便的同学可以采用这种方式

下面我们使用千问模型的 `embedding` 进行测试：

```py
# https://docs.langchain.com/oss/python/integrations/embeddings/dashscope
import os

import numpy as np
from dotenv import find_dotenv, load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings

load_dotenv(find_dotenv())

embeddings = DashScopeEmbeddings(
    model="text-embedding-v1", dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
)

query_list = [
    "机器学习",
    "深度学习",
    "强化学习",
    "大语言模型",
    "智能体",
]

embedding_list = [np.array(embeddings.embed_query(query)) for query in query_list]

# for embbeding_item in embedding_list:
#     print(embbeding_item)

print(
    f"{query_list[0]} 生成长度为 {len(embedding_list[0])} 的 embedding，其前 30 个值为：{embedding_list[0][0:30]}"
)
```

我们已经生成了对应的向量，我们如何度量文档和问题的相关性呢？这里提供两种常用的方法：

- 计算两个向量的点积
- 计算两个向量之间的余弦相似度

点积是将两个向量对应位置的元素相乘之后求和得到的标量值。点积相似度越大，表示两个向量月相似。这里直接使用 numpy 的 dot 函数进行计算：

```py
for i in range(0, len(query_list) - 1):
    for j in range(i + 1, len(query_list)):
        print(
            f'"{query_list[i]}" 与 "{query_list[j]}" 的点积为：{np.dot(embedding_list[i], embedding_list[j])}'
        )
# "机器学习" 与 "深度学习" 的点积为：0.8275871562915844
# "机器学习" 与 "强化学习" 的点积为：0.6015957698292973
# "机器学习" 与 "大语言模型" 的点积为：0.4871444086361928
# "机器学习" 与 "南瓜" 的点积为：0.2838396135901741
# "深度学习" 与 "强化学习" 的点积为：0.6374841367136348
# "深度学习" 与 "大语言模型" 的点积为：0.5706876848085725
# "深度学习" 与 "南瓜" 的点积为：0.2797307143636383
# "强化学习" 与 "大语言模型" 的点积为：0.4921765930753128
# "强化学习" 与 "南瓜" 的点积为：0.23933468900412888
# "大语言模型" 与 "南瓜" 的点积为：0.21115782572566394
```

点积：计算简单，快速，不需要进行额外的归一化步骤，但丢失了方向信息。

余弦相似度：可以同时比较向量的方向和数量级大小。

余弦相似度将两个向量的点积除以他们的模长的乘积。计算公式为：

$$cos(\theta)=\frac{\sum^{n}_{i=1}({x_i}\times{{y_i}})}{{\sum^{n}_{i=1}x_i^2}\times{\sum^{n}_{i=1}y_i^2}}$$

余弦函数的值域在-1到1之间，即两个向量余弦相似度的范围是[-1, 1]。当两个向量夹角为0°时，即两个向量重合时，相似度为1；当夹角为180°时，即两个向量方向相反时，相似度为-1。即越接近于 1 越相似，越接近 0 越不相似。

```py
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
```

目前，我们已经学习了文档的基本处理，但是如何管理我们生成的 embedding 并寻找和 query 最相关的内容呢？难道要每次遍历所有文档么？向量数据库可以帮我们快速的管理和计算这些内容。

## 向量数据库的介绍及使用

### 向量数据库简介

向量数据库是用于高效计算和管理大量向量数据的解决方案。向量数据库是一种专门用于存储和检索向量数据（embedding）的数据库系统。它与传统的基于关系模型的数据库不同，它主要关注的是向量数据的特性和相似性。

在向量数据库中，数据被表示为向量形式，每个向量代表一个数据项。这些向量可以是数字、文本、图像或其他类型的数据。向量数据库使用高效的索引和查询算法来加速向量数据的存储和检索过程。

Langchain 集成了超过 30 个不同的向量存储库。我们选择 Chroma 是因为它轻量级且数据存储在内存中，这使得它非常容易启动和开始使用。

新版本的 LangChain 将 chroma 模块迁移到了 `langchain-chroma` 包中了，并且依赖 `chromadb` 库。

安装依赖：

```bash
pip install langchain-chroma chromadb
```

```py
import os
from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 指定知识库中单段文本长度
CHUNK_SIZE = 500
# 指定知识库中相邻文本重合长度
OVERLAP_SIZE = 50

# 加载环境变量
_ = load_dotenv(find_dotenv())

# 读取文档
script_dir = Path(__file__).parent
file_path = script_dir / ".." / ".." / "data_base" / "knowledge_db" / "pumpkin_book.pdf"
loaders_chinese = [
    PyMuPDFLoader(file_path)
    # 还可以加载其他文档
]
docs = []
for loader in loaders_chinese:
    docs.extend(loader.load())

# 切分文档
# 使用递归字符文本分割器
text_spliter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE, chunk_overlap=OVERLAP_SIZE
)
split_docs = text_spliter.split_documents(docs)

# 定义 embedding
embedding = DashScopeEmbeddings(
    model="text-embedding-v4", dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
)
```

### 构建 Chroma 向量库

上面介绍了文档加载、文档切分的操作，后面将介绍如何将文档进行 embedding，并存入 chroma 向量数据库。

```py
# 构建向量数据库
persist_directory = "../../data_base/knowledge_db/chroma"
vector_store = Chroma(
    embedding_function=embedding,
    persist_directory=persist_directory,  # 允许我们将 persis_directory 目录保存到磁盘上
)

vector_store.add_documents(documents=split_docs[0:100])
```

### 通过向量数据库检索

#### 相似度检索

```py
question = "什么是机器学习"

sim_docs = vector_store.similarity_search(question, k=3)
print(f"检索到的内容数：{len(sim_docs)}")

for i, sim_doc in enumerate(sim_docs):
    print(
        f"检索到的地{i}个内容：\n{sim_doc.page_content[:200]}",
        end="\n-------------------------\n",
    )
```

#### MMR检索

如果只考虑检索出内容的相关性会导致内容过于单一，可能丢失重要信息。

最大边际相关性 (MMR, Maximum marginal relevance) 可以帮助我们在保持相关性的同时，增加内容的丰富度。

核心思想是在已经选择了一个相关性高的文档之后，再选择一个与已选文档相关性较低但是信息丰富的文档。这样可以在保持相关性的同时，增加内容的多样性，避免过于单一的结果。

``` py

```

### 构造检索式问答链

#### 直接询问 LLM

#### 结合 prompt 提问
