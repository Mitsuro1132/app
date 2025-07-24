from django.db import models
from .validators import *

# Create your models here.

class CheckPeople(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(age__gt = 18)

    # def check_full_age(self,age):
    #     return self.get_queryset().filter(age__gt = age)
    
    # def first_person(self):
    #     return self.get_queryset().first()


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    hobby = models.TextField()
    number = models.IntegerField(default=0)

    people = CheckPeople()

    def __str__(self):
        return f'{self.name}--{self.age}--{self.hobby}'
    

    # people = CheckPeople()


class Cars(models.Model):
    TYPE_CAR = [
        ('mechanics','механіка'),
        ('automatics','автомат')
    ]
    name = models.CharField(max_length=20, help_text="Ім'я машини ")
    price = models.DecimalField(blank=True, max_digits=6, decimal_places=5)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='Photo/')
    owner = models.TextField(unique=True, db_index=True)
    description = models.TextField(verbose_name='Опис', null=True)
    updated = models.DateField(auto_now_add=True)
    published = models.DateTimeField(auto_now=True)
    type_car = models.CharField(max_length=30, choices=TYPE_CAR,default='automatics')

    class Meta:
        ordering = ['price']
        db_table = 'db_Cars'
        verbose_name = 'Машина'
        verbose_name_plural = 'Машини'

    def __str__(self):
        return self.name
    
class Man(models.Model):
    name =  models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Business(models.Model):
    business_name = models.CharField(max_length=30)
    man = models.ForeignKey(Man,on_delete=models.CASCADE)
    def __str__(self):
        return self.business_name
    

# відношення один до одного 

class Profile(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def upper_name(self):
        return f"{self.name.upper()}"
    
    def check_age(self):
        if self.age > 18:
            return 'Доросла людина '
        else:
            return 'Мала людина'

class Accoutn(models.Model):
    nickname = models.CharField(max_length=30)

    profile = models.OneToOneField(Profile,on_delete=models.CASCADE,related_name='profile_key')

    def __str__(self):
        return self.nickname
   

# Створення власних  валідаторів 


class Men(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[check_age])




