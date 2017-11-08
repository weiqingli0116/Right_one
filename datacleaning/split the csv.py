import pandas as pd
import os

os.chdir("/Volumes/Don't Panic/WPI/Courses/CS542/Project/Data")

df = pd.read_csv('responses.csv',header = 0)

enjoymusic = df['music']

features = list(df.columns)
#get music and fill all the missing data with 3
musicname = features[1:19]
music = df[musicname]
music = music.fillna(3.0)
music.apply(lambda x: sum(x.isnull()),axis = 0)

#get loved and hated music
def discriminate(x,lovelist,hatelist):
	loved = list()
	hated = list()
	for i in range(len(x)):
		if x[i] > 3:
			loved.append(i+1)
		if x[i] < 3:
			hated.append(i+1)
	lovelist.append(loved)
	hatelist.append(hated)
	return

lmusic = list()
hmusic = list()

music.apply(lambda x: discriminate(x,lmusic,hmusic),axis = 1)

def split(lmusic):
	ori = lmusic
	lmusic = list()
	for i in range(len(ori)):
		for j in ori[i]:
			lmusic.append((i+3,j))
	return lmusic

lmusic = split(lmusic)
hmusic = split(hmusic)
#write in csv
with open("lmusic.csv","w") as f:
	writer = csv.writer(f)
	writer.writerows(lmusic)

with open("hmusic.csv","w") as f:
	writer = csv.writer(f)
	writer.writerows(hmusic)

#get movie and fill all the missing data with 3
moviename = features[20:31]
movie = df[moviename]
movie = movie.fillna(3.0)
movie.apply(lambda x: sum(x.isnull()),axis = 0)

#get loved and hated movie
lmovie = list()
hmovie = list()

movie.apply(lambda x: discriminate(x,lmovie,hmovie),axis = 1)

lmovie = split(lmovie)
hmovie = split(hmovie)
#write in csv
with open("lmovie.csv","w") as f:
	writer = csv.writer(f)
	writer.writerows(lmovie)

with open("hmovie.csv","w") as f:
	writer = csv.writer(f)
	writer.writerows(hmovie)

#get hobbies
hobbyname = features[31:63]
hobby = df[hobbyname]
hobby = hobby.fillna(3.0)
hobby.apply(lambda x: sum(x.isnull()),axis = 0)

lhobby = []
hhobby = []

hobby.apply(lambda x: discriminate(x,lhobby,hhobby),axis=1)

lhobby = split(lhobby)
hhobby = split(hhobby)

with open("lhobby.csv","w") as f:
	writer = csv.writer(f)
	writer.writerows(lhobby)
