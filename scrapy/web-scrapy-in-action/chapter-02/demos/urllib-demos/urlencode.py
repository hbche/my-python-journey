from urllib.parse import urlencode

params = {
    'name': 'hanbin',
    'age': 25
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(params)
print(url)      # https://www.baidu.com?name=hanbin&age=25