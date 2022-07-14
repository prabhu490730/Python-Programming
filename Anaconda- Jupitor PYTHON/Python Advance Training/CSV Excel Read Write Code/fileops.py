#Print the last 5 lines of sample2.txt

f=open("sample2.txt", "r")
lines = f.readlines()
for line in lines[-5:]:
	print(line.rstrip())
f.close()

print("-"*40)

#Print the first 5 lines of sample2.txt
f=open("sample2.txt", "r")
lines = f.readlines()
for line in lines[0:5]:
	print(line.rstrip())
f.close()

print("-"*40)

#Search : Print all lines that contain the word "last" in sample2.txt

f=open("sample2.txt", "r")
for line in f:
	if "last" in line:
		print(line.rstrip())
f.close()

print("-"*40)

#Print the 8th line of sample2.txt
f=open("sample2.txt", "r")
lines = f.readlines()
print(lines[7])
f.close()

print("-"*40)
#Print the number of lines in sample2.txt

f=open("sample2.txt", "r")
lines = f.readlines()
print(len(lines))
f.close()