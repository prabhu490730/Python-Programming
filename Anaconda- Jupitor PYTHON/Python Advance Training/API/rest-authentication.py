import requests
from requests.auth import HTTPBasicAuth

# Making a get request
response = requests.get('https://api.github.com, ',
                        auth = HTTPBasicAuth('user', 'pass'))

# print request object
print(response)

#%%
