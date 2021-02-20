import requests

r = requests.get("https://google.se")
print(r.status_code)
print(r.ok)