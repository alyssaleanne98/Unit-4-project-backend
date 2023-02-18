from django.db import models

# Create your models here.

class Cards(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    #Line 8-9 are two very useful arguments for automatically managing date and time 

    def __str__(self):
        return f'Hello my name is {self.title}'