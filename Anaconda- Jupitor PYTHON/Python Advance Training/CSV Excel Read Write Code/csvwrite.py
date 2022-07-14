# create a csv
import csv

f=open("marks.csv", "w")
writer = csv.writer(f)

header = ["name","math","science","social"]
row1 = ["ramesh",89,98,92]
row2 = ["swapna",90,95,99]

writer.writerow(header)
writer.writerow(row1)
writer.writerow(row2)

f.close()


f=open("marks2.csv", "w")
writer = csv.writer(f)

header = ["name","math","science","social"]
row1 = ["ramesh",89,98,92]
row2 = ["swapna",90,95,99]

writer.writerows([header,row1,row2])

f.close()

#%%
