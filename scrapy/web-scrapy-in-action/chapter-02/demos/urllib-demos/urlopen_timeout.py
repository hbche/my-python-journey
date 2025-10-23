from urllib.request import urlopen
from urllib.error import URLError
import socket

try:
    response = urlopen('https://www.httpbin.org/get', timeout=0.1)
except URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")       # TIME OUT