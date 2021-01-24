import csv
with open("project.csv","r") as file:
    reder = csv.reader(file)
    lis = []
    for row in reder:
        col = row
        print(col)
        s = input("enter status: ")
        lis.append(s)
with open("project.csv","a") as file:
    for i in range(len(lis)):
        writer = csv.writer(file)
        writer.writerow[lis[i]]
