import json

f=open("sample.json", "r")
capitals = json.load(f)
print(capitals.get('India'))
f.close()

#%%
