# file I/O

# write into a file

f=open("sample.txt", "w")
f.write("This is line one\n")
f.write("This is line two\n")
f.write("This is line 3\n")
f.write("This is line 4\n")
f.write("This is the last line")
f.close()


# append to a file

f=open("sample2.txt", "a")
f.write("This is line one\n")
f.write("This is line two\n")
f.write("This is line 3\n")
f.write("This is line 4\n")
f.write("This is the last line")
f.close()

# working with the file pointer

print(f.name)
print(f.mode)
print(f.closed)
#%%
