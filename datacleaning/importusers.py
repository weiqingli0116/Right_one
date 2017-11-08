import csv
from users.models import User

users = list()

 with open('/Volumes/Don\'t Panic/WPI/Courses/CS542/Project/Data/users.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		users.append(row)

del users[0]

for item in users:
	user = User.objects.create_user (username = item[0], first_name = item[1], last_name = item[2], email = item[3], password = "wpi12345")
	user.save



profiles = []
with open('/Volumes/Don\'t Panic/WPI/Courses/CS542/Project/Data/overal-data.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		profiles.append(row)

del profiles[0]
profiles[51]

for item in profiles:
	if item[5] =='no':
		item[5] = False
	else:
		item[5] = True

