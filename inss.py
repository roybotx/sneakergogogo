import requests

url = 'https://api.instagram.com/oauth/authorize/?client_id=3ac6b12d4b33404a856cffa004a6ee76&redirect_uri=https://www.github.com&response_type=code'

r = requests.get(url)

print(r)