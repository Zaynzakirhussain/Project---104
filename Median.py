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


# Find Median
new_data.sort()
n = len(new_data)

if(n % 2 == 0):
    #even
    first_num = new_data[n//2]
    second_num = new_data[n//2 -1]
    median = (first_num + second_num)/2
else:
    #odd
    median = new_data[n//2]

print("The Median is : ", median)