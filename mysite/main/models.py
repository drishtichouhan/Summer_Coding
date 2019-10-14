from django.db import models
from datetime import datetime

class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=255)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField('Date published',default=datetime.now)

	def __str__(self):
		return self.tutorial_title

# Create your models here.
