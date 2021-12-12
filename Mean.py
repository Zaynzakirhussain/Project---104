import csv

with open("Data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

#remove the titles/Headings
file_data.pop(0)

new_data =[]

# get height in a list
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

# Find mean
total = 0

for x in new_data:
    total += x

n = len(new_data)

mean = total/n
print("The mean height is: ", mean)