from celery import shared_task
from celery.exceptions import Retry
from celery.exceptions import SoftTimeLimitExceeded
import time
import logging

@shared_task
def plus(a,b):
    return a + b


@shared_task
def minus(a,b):
    return a - b

@shared_task
def oper1(a,b):
    return a + b

@shared_task
def oper2(a,b):
    return a * b

@shared_task
def oper3(a,b):
    return a / b

@shared_task
def sum_oper(res):
    return sum(res)

@shared_task(soft_time_limit = 20 )
def get_data(a,b):
    try:
        time.sleep(212)
        result = a + b 
        print(f'результат {result}')
        return result
    except SoftTimeLimitExceeded:
        print('long ')
        return "довгий процес "
    
@shared_task(rate_limit = '5/m')
def limit():
    return 'name'


@shared_task
def test_1():
    time.sleep(20)
    return 'test'

@shared_task
def test_2():
    return 'next'

@shared_task
def test_3():
    return 'bam'

