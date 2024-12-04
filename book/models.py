from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=50)
    auther=models.CharField(max_length=30, default='guest')
    email=models.EmailField(blank=True)
    description=models.TextField(max_length=500,default='available')
    image=models.ImageField()

    def __str__(self) -> str:
        return self.name
    