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
