from urllib.request import  urlopen
from urllib.error import HTTPError

response = urlopen('https://ssr3.scrape.center')

try:
    html = response.read().decode('utf-8')
    print(html)
except HTTPError as e:
    print(e.reason)     # urllib.error.HTTPError: HTTP Error 401: Authorization Requiredurllib.error.HTTPError: HTTP Error 401: Authorization Required