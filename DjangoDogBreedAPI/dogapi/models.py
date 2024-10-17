from django.db import models

# Create your models here.
class Breed(models.Model):
    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    trainability = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    sheddingamount = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    exerciseneeds = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, related_name='dogs', on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

