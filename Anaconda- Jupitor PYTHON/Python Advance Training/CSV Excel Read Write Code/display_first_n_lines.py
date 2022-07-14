# accept a file name, line count and
# display as many lines from the beginning of the file

filename    = input("Enter file name : ")
linecount   = int(input("Enter line count :"))

try:
    fileobj     = open(filename,"r")
except FileNotFoundError as fnf:
    print(fnf)
else:
    for no,line in enumerate(fileobj,start=1):
        print(no,":",line.strip())
        if no==linecount:
            break

    fileobj.close()
