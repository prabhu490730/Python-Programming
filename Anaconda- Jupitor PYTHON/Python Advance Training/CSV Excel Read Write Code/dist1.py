# dictionaries

std = {"hyd":"040","blr":"080"}

print(type(std))
print(len(std))
print(std.keys())
print(std.values())
print(std.items())

# how to lookup

print(std.get('hyd'))
print(std['hyd'])

# how to add/update

std['del'] = "011"
std['chennai'] = "088" # wrong entry
std['chennai'] = "044"
print(std)
# how to delete
del std['del']
print(std)

# iterating a dictionary

for key in std:
    print(key)

for key in std:
    print(key,std.get(key))
#%%
