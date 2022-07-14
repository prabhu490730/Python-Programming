import requests

URL = "http://api.open-notify.org/iss-now.json"

response = requests.get(URL)

if response.ok:
    print(response.json())


#%%
