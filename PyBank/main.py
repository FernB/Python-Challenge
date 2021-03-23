import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

csvlist = []
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    next(reader)
    
    
    for row in reader:
        csvlist.append(row)
    

totalmonths = len(csvlist)
total = sum([int(i[1]) for i in csvlist])
averagechange = int(total/totalmonths)
GreatestInc = max(csvlist, key=lambda x: x[1])
GreatestDec = min(csvlist, key=lambda x: x[1])
txtpath = os.path.join('Analysis','financial_analysis.txt')
File = open(txtpath,"w+")
print(f"Financial Analysis\n---------------------------\nTotal Months: {totalmonths}\nTotal: ${total}\nAverage Change: ${averagechange}\nGreatest Increase in Profits: {GreatestInc[0]} (${GreatestInc[1]})\nGreatest Decrease in Profits: {GreatestDec[0]} (${GreatestDec[1]})", file = File)
File.seek(0)
print(File.read())




