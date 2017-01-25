import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=150)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title
		
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.question_text
		
	def was_published_recently(self):
		return self.pub_date >=timezone.now()-datetime.timedelta(days=1)
	
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=150)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.choice_text