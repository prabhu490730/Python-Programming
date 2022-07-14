import json

capitals = {'India':'New Delhi',
            "Russia":'Moscow'}
# Whether you use ' or " JSON will always have the O/P in form of " code.
f=open("sample.json", "w")
json.dump(capitals, f)
f.close()
#%%
