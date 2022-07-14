# reading from a file

# read all lines at once

f=open("sample.txt", "r")
contents = f.read()
print(contents)
f.close()

# read one line at a time

f=open("sample.txt", "r")
print(f.readline())
print(f.readline())
f.close()


# read all lines into a list

f=open("sample.txt", "r")
lines = f.readlines()
print(lines)
f.close()

# use a for loop to read the lines

f=open("sample.txt", "r")
for line in f:
    print(line, end="")
f.close()

print()


f=open("sample.txt", "r")
for line in f:
    print(line.rstrip())
f.close()
#%%
