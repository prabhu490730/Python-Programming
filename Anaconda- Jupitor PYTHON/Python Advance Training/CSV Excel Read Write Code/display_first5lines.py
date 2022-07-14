# accept a file name and dsplay the first 5 lines of the file

filename=input("Enter file name : ")
fileobj = open(filename,"r")

for no,line in enumerate(fileobj,start=1):
    print(no,":",line.strip())
    if no==5:
        break

fileobj.close()
