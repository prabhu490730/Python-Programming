# Accept student name, marks for test 1 and test2 and
# save them in a file called 'marks.txt'. Each value should be separated by a space

filename= "marks.txt"

fileobj = open(filename,"w")

while True:
    name = input("Enter student name (Press Enter to stop): ")
    if not name:
        break
    try:
        mark1 = float(input("Enter mark for test 1 : "))
        mark2 = float(input("Enter mark for test 1 : "))
    except ValueError as ve:
        print("Wrong type of value. ", ve)
        print("Record discarded. Please re-enter")
    else:
        fileobj.write(f"{name} {mark2} {mark2}\n")

fileobj.close()

