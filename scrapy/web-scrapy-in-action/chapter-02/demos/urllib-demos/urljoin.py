from urllib.parse import urljoin

print(urljoin('https://www.baidu.com', 'FAQ.html'))     # https://www.baidu.com/FAQ.html
print(urljoin('https://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))      # https://www.baidu.com/FAQ.html
print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.  html'))     # https://www.baidu.com/FAQ.html
print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.  html?question=2'))      # https://cuiqingcai.com/FAQ.html?question=2
print(urljoin('https://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.    php'))      # https://cuiqingcai.com/index.php
print(urljoin('https://www.baidu.com', '?category=2#comment'))      # https://www.baidu.com?category=2#comment
