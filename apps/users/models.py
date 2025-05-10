from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

	specialization = models.CharField(
		max_length=100,
		blank=True,
		verbose_name='Специализация'
	)

	experience_level = models.CharField(
		max_length=20,
		choices=[
			('junior', 'Junior'),
			('mid', 'Middle'),
			('senior', 'Senior')
		],
		default='junior',
		verbose_name='Уровень опыта'
	)

	def __str__(self):
		return self.username