import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

csvdic = []
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    next(reader)
    
    
    for row in reader:
        csvdic.append(row)
    
    print(len(csvdic))


    total = [int(i[1]) for i in csvdic]
    print(sum(total))





