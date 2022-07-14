# Accept names of few items and
# save them in a file named 'items.txt' in the current directory.

filename="items.txt"

fileobj = open(filename,"w")

while True:
    item = input("Enter item name : ")
    if not item:
        break
    fileobj.write(item+"\n")

fileobj.close()

