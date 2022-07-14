# Accept a file name and a string and
# print all lines from the file which contain the given string

filename = input("Enter file name : ")

search_string = input("Enter search string : ")

try:
    fileobj = open(filename, "r")
except FileNotFoundError as fnf:
    print(fnf)
else:
    for line in fileobj:
        if search_string in line:
            print(line.strip())
    fileobj.close()
