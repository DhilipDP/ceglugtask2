import csv
import os

with open("rotten.csv", "rb") as read:
	reader = csv.reader(read)
	rotten = []
	for row in reader:
		rotten = row
	j = 0
	for i in rotten:
		if i == "1":
			rotten[j] = "t"
		elif i == "0":
			rotten[j] = "f"
		j = j+1

with open("rotten.csv", "wb") as write:
	writer = csv.writer(write)
	writer.writerow(rotten)

emptylist = []

with open("number.csv", "rb") as read:
	reader = csv.reader(read)
	numbers = []
	for i in reader:
		numbers = i
	j = 0
	for i in numbers:
		if i == "" and j % 2 == 0:
			emptylist.append(j)
		elif i == "" and j % 2 != 0:
			numbers[j] = j
		j = j+1

numbers = [x for x in numbers if x != '']



with open("number.csv", "wb") as write:
	writer = csv.writer(write)
	writer.writerow(numbers)

with open("fruits.csv", "rb") as read:
	reader = csv.reader(read)
	fruits = []
	for i in reader:
		fruits = i
	j = 0
	for i in fruits:
		if i == "":
			if j in emptylist:
				pass
			else:
				fruits[j] = fruits[ j - 10 ]
		j = j + 1
	
fruits = [ x for x in fruits if x != "" ]

with open("fruits.csv" , "wb") as write:
	writer = csv.writer(write)
	writer.writerow(fruits)	

rottenlist = []
j = 0

for i in rotten:
	if i == "t":
		rottenlist.append(j)
	j = j + 1

price = []
with open("price.csv", "rb") as read:
	reader = csv.reader(read)
	for i in reader:
		price = i

for i in rottenlist:
	price[i] = 0.00

for i in emptylist:
	del price[i]

for i in emptylist:
	del rotten[i]

j = 0	
for i in price:
	if i == "":
		price[j] = 1.5
	else:
		price[j] = float(i)
	j = j + 1

with open("price.csv", "wb") as write:
	writer = csv.writer(write)
	writer.writerow(price)

with open("data.csv", "wb") as write:
	fieldnames = ["fruit_num", "fruit_name", "fruit_price","fruit_rotten"]
	writer = csv.DictWriter  (write, fieldnames = fieldnames)
	writer.writeheader()
	for i in xrange(100 - len(emptylist)):
		y = {"fruit_num" : numbers[i], "fruit_name" : fruits[i], "fruit_price" : price[i], "fruit_rotten" : rotten[i]}
		writer.writerow(y)

		
