from django.db import models
from users.models import User

# Create your models here.
# The search features


class music(models.Model):
	genre = models.CharField(max_length = 30)

class movie(models.Model):
	genre = models.CharField(max_length = 30)

class hobbies(models.Model):
	hobby_name = models.CharField(max_length = 50)

class health(models.Model):
	SMOKE_CHOICE = (
		(0, 'Never smoked'),
		(1, 'Tried smoking'),
		(3, 'Former smoker'),
		(4, 'Current smoker'),
		)
	DRINK_CHOICE =(
		(0, 'Never'),
		(1, 'Social drinker'),
		(2, 'Drink a lot'),
		)
	smoking = models.IntegerField(choices = SMOKE_CHOICE)
	drinking = models.IntegerField(choices = DRINK_CHOICE)
	health_lifesty = models.IntegerField()
	user = models.ForeignKey ( User, on_delete = models.CASCADE )

	class Meta:
		pass

class spend(models.Model):
	user = models.ForeignKey ( User, on_delete = models.CASCADE )
	save_all = models.IntegerField()
	shopping_center = models.IntegerField()
	branded_clothing = models.IntegerField()
	partying_socializing = models.IntegerField()
	appearance = models.IntegerField()
	gadgets = models.IntegerField()
	food = models.IntegerField()

	class Meta:
		pass

class userfeature(models.Model):
	user = models.OneToOneField( User, on_delete = models.CASCADE)
	enjoymusic = models.IntegerField()
	musicloved = models.ManyToManyField( music, blank = True, related_name ='lmusic')
	musichated = models.ManyToManyField( music, blank = True, related_name ='hmusic')
	enjoymovie = models.IntegerField()
	movieloved = models.ManyToManyField( movie, blank = True, related_name ='lmovie')
	moviehated = models.ManyToManyField( movie, blank = True, related_name ='hmovie')
	hobbies = models.ManyToManyField( hobbies, blank = True)

	class Meta:
		pass








