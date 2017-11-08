import os
import pandas as pd

os.chdir("/Volumes/Don't Panic/WPI/Courses/CS542/Project/Data")

import csv
#load girlname, boyname, lastname
girlname = list()
with open('girlfirstname.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		girlname.append(row)

boyname = list()
with open('boyfirstname.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		boyname.append(row)

lastname = list()
with open('lastname.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		lastname.append(row)

#load users profile
pf = pd.read_csv('overal-data.csv',header = 0)
#genrate other  things
firstname = list()
username = list()
email = list()
nickname = list()

g = 0
b = 0

for u in pf.Gender:
	if u == 'female':
		firstname.append(girlname[g])
		g = g+1
	else:
		firstname.append(boyname[b])
		b = b+1

for u in range(len(firstname)):
	username.append('_'.join(firstname[u] + lastname [u]))
	nickname.append(' '.join(firstname[u] + lastname [u]))
	email.append(''.join(firstname[u]+lastname[u]+["@wmail.com"]))

#save as csv
with open("users.csv","w") as f:
	writer = csv.writer(f)
	writer.writerow(['username','firstname','lastname','email'])
	for i in range(len(username)):
		writer.writerow([username[i],firstname[i][0],lastname[i][0],email[i]])

