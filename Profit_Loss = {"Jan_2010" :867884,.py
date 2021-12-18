import csv
from pathlib import Path
budget_data = Path("Resources/budget_data.csv")
budget_data = []
month = []
pl = []     

#prints header for results
print("Finacial Analyses")
print("--------------------------------------------")

#Counts and prints total number of months
for row in budget_data: 
    month.append(row[0])
    pl.append(row[1])

print(f'Total Months: {len(month)}')
#Finds the sum and prints all values
sum_pl = 0 
for z in pl: 
    sum_pl += int(z)
print(f'Total: ${sum_pl}')



#Finds and prints average change in profit/loss
avg = []
total = 0
for i in range(len(pl)-1): 
    net = int(pl[i+1])-int(pl[i])
        
    avg.append(net)

for x in avg: 
    total += x
    avg_change = total /len(avg)


print(f'Average Change: ${round(avg_change,2)}')

#Finds largest increase in profits
largest = avg [0]
for number in avg : 
    if number > largest:  
        largest = number

date_increase = avg.index(largest)
date_increase = month[date_increase + 1]

print('Greatest increase in profits: {date_increase} $ {largest})')
#Finds largest decrease
smallest = avg [0]
for number in avg : 
    if number < smallest:  
        smallest = number
##########
date_decrease = avg.index(smallest)
date_decrease = month[date_decrease + 1]

print('Greatest decrease in profits: {date_decrease} $ {smallest})')
print("----------------------------------------------------")