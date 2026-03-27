# 前置知识

## 安装依赖

1. 如何将安装的依赖同步到当前 requirements.txt 文件中？

推荐先安装后冻结的方法：

```bash
pip install openai python-dotenv
pip freeze > requirements.txt
```
