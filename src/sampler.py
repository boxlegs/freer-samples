import requests

URL = "https://burberry.freesamples.net.au/TRSYULK8/WFXXJZ/5"

req = requests.get(URL)

print(req.cookies, req.content)