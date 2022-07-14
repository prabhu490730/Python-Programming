marks = [("Hari",45,90,60), ("Garima",65,93,59), ("Sireesha",49,70,79)]

#Sort
print(sorted(marks))

#Sort by Name
print(sorted(marks, key = lambda x:x[0]))

# Sort by Math Marks (1st marks)
print(sorted(marks, key = lambda x:x[1]))

# Sort by English Marks (2nd marks)
print(sorted(marks, key = lambda x:x[2]))

# Sort by Science Marks (3rd marks)
print(sorted(marks, key = lambda x:x[3]))

# Sort by Science Marks- decending Order (3rd marks)
print(sorted(marks, key = lambda x:x[3], reverse= True))

# Sort by Total marks
print(sorted(marks, key = lambda x:sum(x[1:])))
print(sorted(marks, key = lambda x:x[1]+x[2]+x[3]))

#Sorted by length of name
print(sorted(marks, key = lambda x:len(x[0])))
