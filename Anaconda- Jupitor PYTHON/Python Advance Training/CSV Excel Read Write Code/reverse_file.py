# Accept a file name and print the lines in reverse order

filename=input("Enter filename : ")
fileobj=open(filename,"r")
lines=fileobj.readlines()
lines.reverse()

for line in lines:
    print(line.rstrip())

fileobj.close()
