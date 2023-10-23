"""
import csv

companies = []
sales = []

with open ...
    reader = csv.reader(file)
    skip for the first line
    for loop:
        appending to companies
        append sales data - (int, just the sales data, we want a list of tuples)
    

monthly sum (zip) use zip[ to unpack tuples
                          
yearly_sum - put into a dictionary - print(.items method)
for loop

print monthly sales
print .items()
"""
"""
import csv

companies = []
sales = []

with open("carSale.csv", "r") as csvfile:
    lines = file.readlines()
file.close

#for x in range(1, len(lines)):
for x in range(1, 2):
    company_name = lines[x].strip()
    companies.append(company_name)
    company_name = company_name[0]
    #company_name = []


print(companies)
"""

import csv

companies = []
sales = []

with open("carSale.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
            companies.append(row[0])
            sales.append([int(x.replace(",", "")) for x in row[1:]])

print(companies)
print(sales)

yearly_sum = {}
monthly_sum = [sum(x) for x in zip(*sales)]

