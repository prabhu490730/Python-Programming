# Accept a file name and numbe of lines as command line arguments and
# display as many lines from the beginning of the file

import sys

if len(sys.argv)==3:
    print("yes")
    filename=sys.argv[1]
    line_count=int(sys.argv[2])
    
    fileobj = open(filename,"r")

    for no,line in enumerate(fileobj,start=1):
        print(no,":",line.strip())
        if no==line_count:
            break

    fileobj.close()
else:
    print("Please specify filename and linecount")
    
