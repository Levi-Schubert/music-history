from django.db import models

# Create your models here.
class Artist(models.Model):
	artist_name = models.CharField(max_length=100)

	def __str__(self):
		return self.artist_name

class Details(models.Model):
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	details_text = models.CharField(max_length=500)

	def __str__(self):
		return self.details_text