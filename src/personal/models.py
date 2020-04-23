from django.db import models

# Create your models here.
PRIORITY = [ 
    ("L", "Low"), 
    ("M", "Mediun"), 
    ("H", "High"), 
] 


class Question(models.Model):
    title 					= models.CharField(max_length=70)
    question				= models.TextField(max_length=400)
    priority 				= models.CharField(max_length=1, choices=PRIORITY)

    class Meta:
     	verbose_name = "The Question"
     	verbose_name_plural = "Peoples Questions"

    def __str__(self):
        return self.title

BRAND = [
 	("Niagara", "Niagara"),
 	("Phoenix", "Phoenix"),
	("Giant", "Giant"),
 ]

class Bikes(models.Model):
	name 					=models.CharField(max_length=70)
	brand					=models.CharField(max_length=20, choices=BRAND)
	description				=models.TextField(max_length=400)

	class Meta:
		verbose_name = "La bicicleta"
		verbose_name_plural = "Las Bicicletas"

	def __str__(self):
		return self.name

