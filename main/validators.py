from django.core.exceptions import ValidationError 

def check_age(value):
    if value < 18:
        return ValidationError('мала людина')
    
