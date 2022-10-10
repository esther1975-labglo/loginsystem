from django.db import models

class registration(models.Model):
	name = models.CharField(max_length = 10, null = True)
	user_name = models.CharField(max_length = 10)
	password = models.CharField(max_length = 10)
	age = models.IntegerField(default = 20)
	def __str__(self):
		return "{} {} {} {}".format(self.name, self.age, self.user_name, self.password)
		
		

# Create your models here.
