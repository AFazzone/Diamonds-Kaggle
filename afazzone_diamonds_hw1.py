# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("My BU ID ends in 1, I'm analyzing FAIR")
print()

"""Read in the initial diamonds csv, splits into rows"""


infile = open('diamonds.csv', 'r')
diamonds = infile.read()

full_diamond_list = diamonds.split("\n")

"""Creates a list of rows with the word FAIR"""

fair_list =[]
fair = "Fair"

for line in full_diamond_list:
    type = line.split(",")
    if fair in type:
        fair_list.append(line)

#Writes new dataset to Fair CSV
# writing to csv file  
with open('Fair.csv', 'w') as fair_dataset:  
    fair_dataset.write(full_diamond_list[0]+'\n')
    for line in fair_list:
        fair_dataset.write(line +'\n')
    


    
print("Question 1:")
print("The number of entries is ", len(fair_list))

rows = len(fair_list)
total_carat = 0

#Sums all of the carats in column 1 of each row

for row in fair_list:
    row = row.split(",")
    carat = float(row[1])
    total_carat += carat

average_weight = total_carat/rows


print("The average weight is ", round(average_weight,4))

total_price = 0

#Sums all of the prices in column 7 of each row

for i in fair_list:
    i = i.split(",")
    price = int(i[7])
    total_price = total_price + price
    
average_price = total_price/rows

print("The average price is ", round(average_price,4))

# Method A  creates list of price/carat

method_a_list =[]

for e in fair_list:
    e = e.split(",")
    a =float(e[7])/float(e[1])
    method_a_list.append(a)
 
method_a_sum = 0

#sums price/carat

for pw in method_a_list:
    method_a_sum = method_a_sum + pw

method_a_average = method_a_sum/rows

max_ppc = max(method_a_list)
index_max = method_a_list.index(max_ppc)

min_ppc = min(method_a_list)
index_min = method_a_list.index(min_ppc)

#finds the median after sorting the list

method_a_list.sort()


if  len(method_a_list)%2 == 0:
    middle = middle = len(method_a_list)//2
    median_ppc = (method_a_list[middle] + method_a_list[middle-1])/2
else:
    middle = len(method_a_list)//2
    median_ppc = len(middle)

    

print()
print("Question 2:")
print("The average price per carat for method a is", round(method_a_average,4))

# creates a list of prices

method_b_list1 = []
method_b_list2 = []


for x in fair_list:
    x = x.split(",")
    b1 = float(x[7])
    method_b_list1.append(b1)
    
sum_b_list1 = 0

#Sums list of prices

for p in method_b_list1:
    sum_b_list1 = sum_b_list1 + p
    
#Creates a list of carats
    
for y in fair_list:
    y = y.split(",")
    b2 = float(y[1])
    method_b_list2.append(b2)
    
#Sumslist of carats

sum_b_list2 = 0   
 
for w in method_b_list2:
    w = float(w)
    sum_b_list2 = sum_b_list2 + w

method_b_average = sum_b_list1/sum_b_list2
    
print("The average price per carat for method b is", round(method_b_average,4))

#Figures out which is lower

if method_a_average < method_b_average:
    print("Method A is lower")
else:
    print("Method B is lower")

print("The maximum price per carat is ", round(max_ppc,4))
print("The minimum price per carat is ", round(min_ppc,4))
print("The median price per carat is ", round(median_ppc,4))




print()
print("Question 3")

#Finds the other paramaters for min/max

def diamond_parameters (list_row):
    values = list_row.split(",")
    print("cut: ",values[2],", color: ",values[3],", clarity:",values[4],
          ", depth: ",values[5],", table ",values[6])
       

print("The paramaters for the highest value are:")
diamond_parameters(fair_list[index_max])


print("The paramaters for the least value are:")
diamond_parameters(fair_list[index_min])


print()
print("Question 4")

high = "${:,.2f}".format(max_ppc * 102)
low = "${:,.2f}".format(min_ppc * 102)

print("My price range for a 102 carat diamond is between ", low, "and", high)





