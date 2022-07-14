# Accept a file name and print the last line

filename=input("Enter file name :")

try:
    fileobj = open(filename,"r")
except FileNotFoundError as fnf:
    print(fnf)
else:
    lines = fileobj.readlines()
    print(lines[-1])
    fileobj.close()
