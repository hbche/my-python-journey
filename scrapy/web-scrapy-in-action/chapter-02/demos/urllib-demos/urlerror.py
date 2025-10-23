from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import socket

try:
    response = urlopen('https://cuiqingcai.com/404', timeout=0.01)
except HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except URLError as e:
    print(type(e.reason))       # <class 'TimeoutError'>
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')       # TIME OUT
    