from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader

# 使用脚本所在目录的绝对路径
script_dir = Path(__file__).parent
file_path = script_dir / ".." / ".." / "data_base" / "konwledge_db" / "pumpkin_book.pdf"

loader = PyMuPDFLoader(file_path)
pages = loader.load()

print(f"每页文档类型：{type(pages[1])}\n")
print(f"第2页文档描述信息：\n{pages[1].metadata}")
print(f"第2页文档内容：\n{pages[1].page_content[0:]}")
