import requests
from requests.auth import HTTPBasicAuth

def test_basic_auth():
    url = "http://api.github/users"
    response = requests.get(url,auth=HTTPBasicAuth('Ashley','Pwd123'))
    print(response.text)
