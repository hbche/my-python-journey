from langchain_community.document_loaders import PyMuPDFLoader

# 创建一个 PyMuPDFLoader 实例，输入为待加载的 pdf 文档路径
loader = PyMuPDFLoader(".\\data_base\\konwledge_db\\pumpkin_book.pdf")

# 调用 PyMuPDFLoader 的load方法对 pdf 文件进行加载
pages = loader.load()

print(f"载入后的变量类型为：{type(pages)}，该PDF一共含有{len(pages)}页\n")

page = pages[1]
print(f"文档的类型为：\n{type(page)}")
print(f"第一页文档的描述信息为：\n{page.metadata}")
print(f"第一页文档的内容为：\n{page.page_content[0:1000]}")
