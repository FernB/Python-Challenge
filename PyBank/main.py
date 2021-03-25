import os
import csv

#creates path from within PyBank Resources folder
dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname,'Resources','budget_data.csv')

#setting all loop counters to empty or 0
totalmonths = 0
net = 0
maxchange = 0
maxdate = ""
minchange = 0
mindate = ""
change = 0
changetotal = 0  
total = 0  

#opens csv and returns object containing rows
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    #skips the headers
    csv_header = next(reader)
    #loops through each row of csv file
    for row in reader:
        #counts months and tallys net profit/loss but ensures first row isn't counted towards the average change 
        if totalmonths == 0:
            totalmonths = totalmonths + 1
            total = total + int(row[1])
            net = int(row[1])
        else:
            totalmonths = totalmonths + 1
            total = total + int(row[1])
            change = int(row[1]) - net
            net = int(row[1])
            changetotal = changetotal + change
            #if to find max and min change    
            if change > maxchange:
                maxchange = change
                maxdate = row[0]   
            elif change < minchange:
                minchange = change
                mindate = row[0]       
#creates path for txt file within PyBank Analysis folder
txtpath = os.path.join('Analysis','financial_analysis.txt')
#opens file to write and will overwrite existing content if analysis has been previously performed
File = open(txtpath,"w+")
#prints analysis to file
print(f"Financial Analysis\n---------------------------\nTotal Months: {totalmonths}\nTotal: ${total}\nAverage Change: ${changetotal/(totalmonths-1):.2f}\nGreatest Increase in Profits: {maxdate} (${maxchange})\nGreatest Decrease in Profits: {mindate} (${minchange})", file = File)
#prints content of file to command line, starting from begining of file
File.seek(0)
print(File.read())




