import csv

file = '/home/ubuntu/Desktop/PPFL/daic_woz_dataset/full_test_split.csv'

data = []
with open(file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            data.append(row)
for i in data:
    print(i)
