#dependancies
import os
import csv

#creates path to data file from PyPoll Resoucres folder
dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname,'Resources','election_data.csv')

#sets empty dictionary and vote counter to capture candinate data from loop
results = {}
totalvotes = 0

#opens csv and returns object containing iterable rows
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    #skips header and stores for future reference
    csv_header = next(reader)
    #loops through each row 
    for row in reader:
        #tallies total number of votes
        totalvotes = totalvotes + 1
        #checks if candidate is in dictionary yet
        if results.get(row[2]) == None:
            #if not then adds name as dictionary key and initialises candidate vote count as value
            counter = 1
            results[row[2]] = counter
        else:
            #if already in dictionary then obtains current count, adds to count and sets against the key
            counter = results[row[2]] + 1
            results[row[2]] = counter            
#creates path for txt file within PyPoll Analysis folder
txtpath = os.path.join(dirname,'Analysis','results.txt')
#opens/creates file to read/write and will overwrite exisiting content if analysis has been previously performed
File = open(txtpath,"w+")
#prints to file
print("Election Results\n-----------------", file = File)
print(f"Total Votes: {totalvotes}\n-----------------", file = File)

#prints candidates results from result dictionary to file
for candidate in results:
    print(f"{candidate}: {(results[candidate]/totalvotes*100): .3f}% ({results[candidate]})", file = File)

#obtains winner based on max vote count
winner = max(results, key=results.get)
#prints winner to file
print(f"-----------------\nWinner: {winner}\n-----------------", file = File)
#prints content of file to command line starting from begining of file
File.seek(0)
print(File.read())