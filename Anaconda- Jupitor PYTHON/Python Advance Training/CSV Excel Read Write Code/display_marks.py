# Dsplay marks stored in 'marks.txt'
# Each valuein a record is separated by a space

filename= "marks.txt"

try:
    fileobj = open(filename,"r")
except FileNotFoundError as fnf:
    print(fnf)
else:
    print("Name \tTest1 \tTest2")
    for line in fileobj:
        name,mark1,mark2=line.strip().split()
        print(f"{name}\t{mark1}\t{mark2}")

    fileobj.close()

