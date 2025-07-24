from django.db import models

# Create your models here.
class Whiskey(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    mocnist = models.IntegerField()
    description = models.TextField(blank=False)
    release_data = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 