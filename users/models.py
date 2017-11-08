from django.db import models
from django.contrib.auth.models import AbstractUser

from types import MethodType
import os

AVATAR_ROOT = 'static/media/avatar'
AVATAR_DEFAULT = os.path.join(AVATAR_ROOT, 'default.jpeg')


class User(AbstractUser):
	nickname = models.CharField(max_length = 50, blank = True)
	intro = models.CharField(max_length = 500, blank = True)
	avatar = models.ImageField(upload_to=AVATAR_ROOT, default = AVATAR_DEFAULT)

	class Meta(AbstractUser.Meta):
		pass

class profile(models.Model):
	GENDER = (
		('F', 'female'),
		('M', 'male'),
		)
	EDUCATION =(
		(0, 'currently a primary school pupil'),
		(1, 'primary school'),
		(2, 'secondary school'),
		(3, 'college/bachelor degree'),
		(4, 'masters degree'),
		(5, 'doctorate degree')
		)
	user = models.OneToOneField(User, on_delete = models.CASCADE,)
	age = models.IntegerField()
	height = models.IntegerField()
	weight = models.IntegerField()
	gender = models.CharField(max_length = 1, choices = GENDER)
	education = models.IntegerField(choices = EDUCATION)
	only_child = models.BooleanField()
	location = models.CharField(max_length = 2)
	class Meta:
		pass

# Create your models here.
