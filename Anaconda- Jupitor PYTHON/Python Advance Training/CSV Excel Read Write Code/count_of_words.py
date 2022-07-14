# Accept a file name and display total number of words in the file

filename = input("Enter file name : ")

try:
    fileobj = open(filename,"r")
except FileNotFoundError as fnf:
    print("Sorry, file not found")
else:

    print("No of words : ",len(fileobj.read().split()))
    
    fileobj.close()
