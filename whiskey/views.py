from django.shortcuts import render,redirect,get_object_or_404
from .models import Whiskey
from .forms import CreateWhiskeyForm
from django.views.decorators.cache import cache_page
from django.core.cache import cache 
from django.http import JsonResponse
# from . redis_client import r,REDIS_KEY
from redis.exceptions import LockError
from .tasks import *
from celery import chain,group,chord
# Create your views here.


# @cache_page(60)
# def all_product(request):
#     products = Whiskey.objects.all()
#     return render(request,'all_products.html',{'products': products})


# def get_redis_data(request):
#     # r.rpush(REDIS_KEY, 'Sasha')
#     # r.rpush(REDIS_KEY, 'Roma')
#     # r.delete(REDIS_KEY)
#     r.lpop(REDIS_KEY)
#     count = r.llen(REDIS_KEY)
#     all_data = r.lrange(REDIS_KEY, 0,-1)
#     return JsonResponse({
#         'name': all_data,
#         'count':count,
#     })

# def get_redis_data(request):
#     data = Whiskey.objects.values_list('name','price')
#     for name,price in data:
#         r.rpush(REDIS_KEY,f'{name},{price}')

#     all_data = r.lrange(REDIS_KEY, 0,-1)
#     return JsonResponse({
#         'name': all_data,
#     })



# def all_product(request):
#     key = 'all'  
#     products = cache.get(key)
#     if products is None:
#         products = Whiskey.objects.all()
#         cache.set(key, products, None) 
#     return render(request, 'all_products.html', {'products': products})

# def all_product(request):
#     ip = request.META['REMOTE_ADDR']
#     key_user = f'access {ip}' 
#     limit = 5 
#     period = 10*60

#     current = cache.get(key_user)

#     if current is None:
#         cache.set(key_user,1, period)
#     elif int(current) >= limit:
#         return JsonResponse({'error': 'get out'},status =429)
#     else:
#         cache.incr(key_user)

#     products = Whiskey.objects.all()
#     return render(request, 'all_products.html', {'products': products})    

# def all_product(request):
#     cache_key = 'all'
#     lock_key = 'lock:all'

#     # 1. Перевіряємо кеш
#     products = cache.get(cache_key)
#     if products is not None:
#         return render(request, 'all_products.html', {'products': products})

#     # 2. Спроба захопити lock
#     try:
#         with r.lock(lock_key, timeout=30, blocking_timeout=5):
#             # 3. Double check кеш, раптом інший вже його створив
#             products = cache.get(cache_key)
#             if products is not None:
#                 return render(request, 'all_products.html', {'products': products})

#             # 4. Якщо кеш все ще порожній — робимо запит у БД
#             products = Whiskey.objects.all()

#             # 5. Кладемо в кеш
#             cache.set(cache_key, products, 60 * 15)

#             return render(request, 'all_products.html', {'products': products})
#     except LockError:
#         # 6. Якщо lock не вдалося захопити — fallback
#         products = cache.get(cache_key)
#         if products is not None:
#             return render(request, 'all_products.html', {'products': products})
#         return render(request, 'all_products.html', {'products': []})


# def all_product(request):
#     key_product = 'all_product'
#     fallback_key = 'fallback_product'
    
#     products = cache.get(key_product)
#     if products:
#         return render(request, 'all_products.html',{'products':products})

#     try:
#         products = Whiskey.objects.all()
#         cache.set(key_product,products,timeout=10*60)
#         cache.set(fallback_key,products,timeout=3600)
#         return render(request, 'all_products.html',{'products':products})
#     except Exception as e:
#         products = cache.get(fallback_key)
#         if products:
#             return render(request, 'all_products.html',{'products':products})
#         return render(request, 'all_products.html',[])
        
def all_products(request):
    products = Whiskey.objects.all()
    # plus.delay(4,5)
    # minus.apply_async((10,5),eta=10)
    # data = group(
    #     oper1.s(5,9),
    #     oper2.s(10,14),
    #     oper3.s(20,8),
    # )()

    # data = chain(
    #     oper1.s(1,2),
    #     oper2.s(5),
    #     oper3.s(2)
    # )()

    # data = chord(
    #     [
    #         oper1.s(1,2),
    #         oper2.s(10,3),
    #         oper3.s(9,3)
    #     ],
    #     sum_oper.s()
    # )()

    # plus.apply_async(args=(1, 2), queue='this')
    # oper1.delay(1,2)
    # oper2.apply_async(args=(1, 2), queue='this')
    # oper3.apply_async(args=(1, 2), queue='data')
    # plus.delay(1,2)
    # plus.delay(1,2)
    # for i in range(20):
    #     limit.delay()
    test_1.delay()
    test_2.delay()
    test_3.delay()

    

    return render(request, 'all_products.html',{'products':products})


def create_product(request):
    if request.method == 'POST':
        form = CreateWhiskeyForm(request.POST)
        if form.is_valid():
            form.save()
            cache.delete('all')
            return redirect('/')
    else:
        form = CreateWhiskeyForm()

    return render(request,'create_whiskey.html',{'form':form})

def product_details(request,id):
    key_detail = f"detail - {id}"
    product = cache.get(key_detail)
    if product is None:
        product = get_object_or_404(Whiskey,id = id)
        cache.set(key_detail,product,10*60) 
    return render(request,'product_details.html',{'product': product})

def update_product(request,id):
    product = get_object_or_404(Whiskey,id = id)
    if request.method == 'POST':
        form = CreateWhiskeyForm(request.POST,instance = product)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateWhiskeyForm()
    return render(request, 'update_product.html',{'form': form})


def delete_product(request,id):
    product = Whiskey.objects.get(id = id)
    product.delete()
    return redirect('/')


