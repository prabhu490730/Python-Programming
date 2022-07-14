# Accept a fle name and display the file along with line numbers

filename=input("Enter file name : ")
fileobj = open(filename,"r")

for no,line in enumerate(fileobj,start=1):
    print(no," : ",line.strip())

fileobj.close()
