from django.db import models

# Create your models here.

class Diary(models.Model):
    tittle = models.CharField(max_length=255)
    description = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.tittle