import os
import csv


csvpath = os.path.join('Resources','election_data.csv')

results = {}
totalvotes = 0

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(reader)
    
    for row in reader:
        totalvotes = totalvotes + 1
        if results.get(row[2]) == None:
            counter = 1
            results[row[2]] = counter
        else:
            counter = results[row[2]] + 1
            results[row[2]] = counter            

txtpath = os.path.join('Analysis','results.txt')
File = open(txtpath,"w+")
print("Election Results\n-----------------", file = File)
print(f"Total Votes: {totalvotes}\n-----------------", file = File)

for candidate in results:
    print(f"{candidate}: {(results[candidate]/totalvotes*100): .3f}% ({results[candidate]})", file = File)

winner = max(results, key=results.get)

print(f"-----------------\nWinner: {winner}\n-----------------", file = File)
File.seek(0)
print(File.read())