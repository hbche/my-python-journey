# 第 17 章 使用 API

## 17.1 使用 API

### 17.1.1 Git 和 Github

### 17.1.2 使用 API 调用请求数据

GitHub 的 API 让我们能够调用 API 请求各种信息。

```bash
https://api.github.com/search/repositories?q=language:python+sort:starts
```

这个 API 调用返回 GitHub 当前托管了多少个 Python 项目，以及有关最受欢迎的 Python 仓库的信息。

repositories 后面的问号指出需要传递一个参数。参数 q 表示查询，而等号(=)让我们能够开始指定查询(q=)。接着，通过 language:python 指出只想获取主要语言为 Python 的仓库的信息。最后的+sort:stars 指定将项目按星数排序。

### 17.1.3 安装 Requests

Requests 包让 Python 程序能够轻松地向网站请求信息并检查返回的响应。

```bash
python -m pip install --user requests
```

### 17.1.4 处理 API 响应

```python
import requests

# 执行 API 调用并查看响应
url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:starts+starts:>10000'

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")          # Status Code: 200

# 将响应转换成字典
response_dist = r.json()

print(response_dist.keys())                     # dict_keys(['total_count', 'incomplete_results', 'items'])
```

我们调用 get()并将变量 url 和 headers 传递给它，再将响应对象存储在变量 r 中。响应对象包含一个名为 status_code 的属性，指出请求是否成功（状态码 200 表示请求成功）​。我们打印 status_code，以核实调用是否成功。使用 json()方法将这些信息转换为一个 Python 字典，并将结果赋值给变量 response_dict。

### 17.1.5 处理响应字典

将 API 调用返回的信息存储到字典里后，就可处理其中的数据了。生成一些概述这些信息的输出是一种不错的方式，可帮助我们确认收到了期望的信息，进而开始研究感兴趣的信息：

```python
import requests

# 执行 API 调用并查看响应
url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'


headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")          # Status Code: 200

# 将响应转换成字典
response_dict = r.json()

# 处理响应字典
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# 研究第一个仓库
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
```

下面来提取与一些键相关的值：

```python
import requests

# 执行 API 调用并查看响应
url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'


headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")          # Status Code: 200

# 将响应转换成字典
response_dict = r.json()

# 处理响应字典
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# 研究第一个仓库
repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")
```

### 17.1.6 概述最受欢迎的仓库

在对这些数据进行可视化时，我们想涵盖多个仓库。下面就来编写一个循环，打印 API 调用返回的每个仓库的特定信息，以便能够在图形中包含这些信息：

```python
import requests

# 执行 API 调用并查看响应
url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'


headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")          # Status Code: 200

# 将响应转换成字典
response_dict = r.json()

# 处理响应字典
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# 研究第一个仓库
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
```

### 17.1.7 监控 API 的速率限制

## 17.2 使用 Plotly 可视化仓库

```python
import requests
import plotly.express as px

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'
headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
response_dict = r.json()

repo_dicts = response_dict['items']
print(len(repo_dicts))

repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

print(repo_names)
print(stars)

fig = px.bar(x=repo_names, y=stars)
fig.show()
```
