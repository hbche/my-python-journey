import os

from dotenv import find_dotenv, load_dotenv
from langchain_chroma.vectorstores import Chroma
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

_ = load_dotenv(find_dotenv())

loader = PyMuPDFLoader("../../data_base/knowledge_db/pumpkin_book.pdf")
documents = loader.load()

CHUNK_SIZE = 500
CHUNK_VERLAP = 150
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_VERLAP
)
docs = text_splitter.split_documents(documents)

embedding = DashScopeEmbeddings(
    model="text-embedding-v4", dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
)

persist_directory = "../../data_base/konwledge_db/chroma"
vectordb = Chroma.from_documents(
    documents=docs, embedding=embedding, persist_directory=persist_directory
)

question = "什么是机器学习"
matching_docs = vectordb.max_marginal_relevance_search(question, k=3)
for i, matching_doc in enumerate(matching_docs):
    print(
        f"第 {i + 1} 个匹配的内容：\n{matching_doc.page_content}",
        end="\n---------------\n",
    )
