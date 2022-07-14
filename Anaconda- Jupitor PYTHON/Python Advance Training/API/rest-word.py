import requests
URL = 'http://garuda.pythonanywhere.com/words'

#GET Method: Fetch the meaning of "water" from URL Dictionary //Case Sensitive
print(requests.get(URL + "/water").json())


#POST Method
print(requests.get(URL + "/wellsfargo").json()) #Check if you've word available
payload = {"word":"wellsfargo", "meaning":"bank"}
print(requests.post(URL, data=payload).json())
    #Request GET again to see the value
print(requests.get(URL + "/wellsfargo").json())


#PUT Method: To Update the Existing Word
payload = {"word":"wellsfargo", "meaning":"A Global bank based in USA"}
print(requests.put(URL, data=payload).json())
    #Request GET again to see the value updated
print(requests.get(URL + "/wellsfargo").json())


# DELETE Method:
print(requests.delete(URL + "/wellsfargo").json())
    #Request GET again to see the value deleted
print(requests.get(URL + "/wellsfargo").json())

#%%
