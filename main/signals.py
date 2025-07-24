from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from  . models import Person

@receiver(pre_save,sender = Person)
def before_create(sender,instance,**kwargs):
    # instance.name = instance.name.upper()
    if instance.name == "Sasha":
        instance.name = instance.name.upper()
    else:
        print("міняти ім'я можемо міняти тільки Sasha")

@receiver(post_save,sender = Person)
def notify_create(sender,instance,created,**kwargs):
    if created:
        print(f'Ви створили людину {instance.name}')
    else:
        print('ви не створили людину')

@receiver(pre_delete,sender = Person)
def before_delete_person(sender,instance,**kwargs):
    print(f'Ви хочете видалити людину  {instance.name}')

@receiver(post_delete,sender=Person)
def delete_person(sender,instance,**kwargs):
    print('Ви видалили людину')

