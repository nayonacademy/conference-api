from django.db import models
# Create your models here.
# from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
# from model_utils import Choices

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ConfOwnProfile(models.Model): 
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	reviews = models.CharField(max_length=100)
	reads = models.CharField(max_length=100)
	useful = models.CharField(max_length=100)
	attend = models.CharField(max_length=100)
	favourite = models.CharField(max_length=100)
	picture = models.CharField(max_length=100)

class Conference (models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=244)
	website = models.CharField(max_length=244)
	about = models.TextField()
	phone = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	address = models.CharField(max_length=244)
	city = models.CharField(max_length=100)
	zipCode = models.CharField(max_length=100)
	speakers = models.CharField(max_length=100)
	facebook = models.CharField(max_length=100)
	twitter = models.CharField(max_length=100)
	instagram = models.CharField(max_length=100)
	organizerID = models.CharField(max_length=100)
	locations = models.CharField(max_length=100)

class ConferenceTest (models.Model):
	name = models.CharField(max_length=100)
	speaker = models.CharField(max_length=100)

class Location (models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	conference = models.ForeignKey(Conference,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	time = models.CharField(max_length=100)

class Rating (models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	conference = models.ForeignKey(Conference,on_delete=models.CASCADE)
	rate = models.CharField(max_length=100)
	comment = models.CharField(max_length=100)
	caption = models.CharField(max_length=100)
	attendQ = models.CharField(max_length=100)
	enjoyQ = models.CharField(max_length=100)
	locationQ = models.CharField(max_length=100)
	connectPeerQ = models.CharField(max_length=100)
	awesome = models.CharField(max_length=100)
	great = models.CharField(max_length=100)
	average = models.CharField(max_length=100)
	poor = models.CharField(max_length=100)
	terrible = models.CharField(max_length=100)
	favorite = models.CharField(max_length=100)
	like = models.CharField(max_length=100)

class Report (models.Model):
	offensive = models.CharField(max_length=100)
	violence = models.CharField(max_length=100)
	spam = models.CharField(max_length=100)
	appropriate = models.CharField(max_length=100)

class Speaker (models.Model):
	name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)

class Claim(models.Model):
	fullname = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	website = models.CharField(max_length=100)
	conference_name = models.CharField(max_length=100)
	street_address = models.TextField()
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=100)
