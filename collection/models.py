from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField(unique=True)

# Create your models here.
