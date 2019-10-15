from django.db import models
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
	Name = models.CharField(max_length=200)
	Place = models.ForeignKey(
		'auth.User',
		on_delete=models.CASCADE,
	)
	text = models.TextField()

	def __str__(self):
		return self.Name

	def get_absolute_url(self):
		return reverse('home')

	