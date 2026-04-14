# 基于 GoogleAI + Chroma向量数据库
import os

from dotenv import find_dotenv, load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.embeddings import DashScopeEmbeddings

# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

_ = load_dotenv(find_dotenv())

# 加载文档
loader = PyMuPDFLoader("../../data_base/knowledge_db/pumpkin_book.pdf")
documents = loader.load()


# 切割文档
CHUNK_SIZE = 500
CHUNK_OVERLAP = 150
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
)
docs = text_splitter.split_documents(documents)

# 向量化
# embedding = GoogleGenerativeAIEmbeddings(
#     model="gemini-embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY")
# )

embedding = DashScopeEmbeddings(
    model="text-embedding-v4", dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
)

persist_directory = "../../data_base/knowledge_db/chroma"
vectordb = Chroma.from_documents(
    documents=docs, embedding=embedding, persist_directory=persist_directory
)


# 测试检索
question = "什么是机器学习"
matching_docs = vectordb.similarity_search(question, k=3)
for i, matching_doc in enumerate(matching_docs):
    print(
        f"第 {i + 1} 个匹配的内容：\n{matching_doc.page_content}",
        end="\n---------------\n",
    )
