import os

import csv

#print(os.getcwd())

list_of_names = []
unique_list = []
results = []


input_path = os.path.join('..','PyPoll','election_data.csv')
output_path = os.path.join('output_file.csv')

with open(input_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #csv_header = next(csvreader)
    next(csvreader,None)
    
    for row in csvreader:
        list_of_names.append(row[2])
        if row[2] not in unique_list:
            unique_list.append(row[2])
            
    print(str(unique_list))
    
    dictionary = { i : 0 for i in unique_list }
    
    for name in list_of_names:
        dictionary[name] += 1
        
    print(str(dictionary))
    
    
    total_votes = len(list_of_names)
    
    def percent_vote(number):
        percent = (number / total_votes)
        return '%.3f' % (percent * 100)
    
    
    line1 = ("Election Results")
    line2 = ("-------------------------")
    line3 = ("Total Votes:  " + str(total_votes))
    line4 = ("-------------------------")
    for x in dictionary:
        value = dictionary[x]
        key = x
        y = (str(key) + ":  " + str((percent_vote(int(value)))) + "%  (" + str(dictionary[x]) + ")")
        results.append(y)
        
    line6 = ("-------------------------")
    line7 = ("Winner:  " + max(dictionary, key=dictionary.get))
    
    
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    for result in results:
        print(result)
    print(line6)
    print(line7)
    
    
        
    with open(output_path, 'w', newline='') as output_file:

    # Initialize csv.writer
        csvwriter = csv.writer(output_file, delimiter=',')

        csvwriter.writerow([str(line1)])
        csvwriter.writerow([str(line2)])
        csvwriter.writerow([str(line3)])
        csvwriter.writerow([str(line4)])
        for result in results:
            csvwriter.writerow([str(result)])
        csvwriter.writerow([str(line6)])
        csvwriter.writerow([str(line7)])