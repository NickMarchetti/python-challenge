import os

import csv

#print(os.getcwd())

total_months = 0
months = []
total_profit = 0
rev_change = []
revenues = []

input_path = os.path.join('budget_data.csv')
output_path = os.path.join('output_file.csv')

with open(input_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#   csv_header = next(csvreader)
    next(csvreader,None)
    
    for row in csvreader:
#       print(row)
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        revenues.append(int(row[1]))
        months.append(row[0])
        
    for x in range(1,len(revenues)):
        rev_change.append(revenues[x] - revenues[x-1])
        average_change = sum(rev_change) / len(rev_change)
        max_change = max(rev_change)
        min_change = min(rev_change)
        max_date = months[(rev_change.index(max_change))]
        min_date = months[(rev_change.index(min_change))]
    
        
    line1 = ("Total months:  " + str(total_months))
    line2 = ("Total Profits/Losses:  $" + str(total_profit))
    line3 = ("Average Change:  $" + str(round(average_change,2)))
    line4 = ("Greatest Increase in Profits:  " + str(max_date) + "  ($" + str(max_change) + ")")
    line5 = ("Greatest Decrease in Profits:  " + str(min_date) + "  ($" + str(min_change) + ")")
    
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    
    with open(output_path, 'w', newline='') as output_file:

    # Initialize csv.writer
        csvwriter = csv.writer(output_file, delimiter=',')

        csvwriter.writerow([str(line1)])
        csvwriter.writerow([str(line2)])
        csvwriter.writerow([str(line3)])
        csvwriter.writerow([str(line4)])
        csvwriter.writerow([str(line5)])