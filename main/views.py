from django.db.models import F,Case,When,CharField,Value
from django.db.models import Avg, Min, Max, Sum
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from . models import Person,Man,Business,Profile,Accoutn


# Create your views here.

def get(request):
    return HttpResponse('hello')

def get_request(request):
    return HttpResponse('privet')

def numb(request):
    return HttpResponse('qqwweeeert')

def next_step(request,a,b,c):
    return HttpResponse(f'{a+b+c}')

def strok(request,a,b):
    if a==b:
        return HttpResponse('+')
    else:
        return HttpResponse('-')
    
def templ(request):
    return render(request,"index.html")

def step(request):
    return render(request,"step.html")

def test(request):
    a = 666
    data = {"key1": a}
    return render (request,'index2.html', data)

def test_dict(request):
    data2 ={'name': 'sasha',
            'age': 18,
            'hobby': 'IT'}
    return render(request,'index3.html', data2)

def  Yulian_gey(request):
     yulian = [1,2,3,4,5]
     a = {'key3': yulian}
     return render (request, 'index4.html',a)

def Roma_warface(request):
    name = request.GET.get("name",'Yulian')
    age = request.GET.get("age",'100')
    return HttpResponse(f'{name} - {age}')

def view1(request):
    return HttpResponseRedirect('/test')

def data(request):
    return render (request, 'data.html')

def post_data(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    return HttpResponse(f'{name}-{age}')

def iphone13(request):
    return render (request,'Iphone13.html')

def iphone15(request):
    return render (request,'Iphone15.html')

# people = Person.objects.all()
# print(people.query)
# for i in people:
#     print(i.id,i.name,i.age,i.hobby)
"""people = Person.objects.get(id = 1)
print(people.id,people.name,people.age,people.hobby)""" # виводиться певний елемент таблиці

# def get_new(request):
#     people = Person.objects.all()
#     return render (request, 'new.html',{'new_key': people})

# variable = Person.objects.create(name = 'Sasha', age = 18, hobby = 'IT')
# people = Person.objects.all()
# for i in people:
#     print(i.name,i.age,i.hobby)

# people = Person(name = 'Inna', age = 18, hobby = 'Paint')
# people.save()

# Фільтрація 


# people = Person.objects.filter(age = 18)
# for i in people:
#     print(i.age,i.name)

# people = Person.objects.exclude(name = 'Sasha')
# for i in people:
#     print(i.name,i.age)

#  оператори 

# people = Person.objects.filter(age__gt = 18)
# for i in people:
#     print(i.age,i.name)

"""people = Person.objects.all()
for i in people:
    print(i.age,i.name)"""

# people = Person.objects.filter(age__in = [18,24])
# for i in people:
#     print(i.name,i.age)

'''people = Person.objects.filter(age__range = (18,40))
for i in people:
    print(i.name,i.age)'''

# delete 

# people = Person.objects.all()
# for i in people:
#     print(i.id,i.name,i.age)

# people = Person.objects.get(id = 4 )
# people.delete()


# people = Person.objects.all()
# for i in people:
#     print(i.id,i.name,i.age)

# Оновлення

# people  = Person.objects.get(id = 3)
# people.name = 'maks'
# people.save()


# people = Person.objects.all()
# for i in people:
#     print(i.id,i.name,i.age)

# сортування 

'''people =  Person.objects.order_by('-age')
for i in people:
    print(i.age,i.name)'''

# певний набір значень та ключів

'''people = Person.objects.values_list('id','name')
print(people)'''

'''people = Person.objects.values('id','name') # список словників
print(people)'''

# отримання списку певного ключа

'''people = Person.objects.values_list('name',flat=True )
print(people)'''


# отримання першого та останнього елемента 

'''people = Person.objects.first() # last або first
print(people.name,people.age)
'''

# агрегатні функції

'''people = Person.objects.aggregate(Sum("age"))
print(people)'''

# people = Person.objects.values_list('name').distinct() #  без дублювання
# print(people)

# people = Person.objects.all()#([
#     Person(name = ' Sasha',age = 19, hobby = 'IT'),
#     Person(name = 'Oleg', age = '12', hobby = 'Football'),
# ])
# for i in people:
#     print(i.name,i.age)

# Обмеження таблиць

# відношення таблиць
'''man = Man.objects.create(name = 'Maks',age = 19)'''
# man = Man.objects.get(id = 1)
# business = Business.objects.create(business_name = 'LEGO', man= man)

# man = Man.objects.create(name = 'Vlad' , age = 18)

# business = Business.objects.create(business_name = 'monopoly',man=man)

'''man = Man.objects.get(id = 1)
businesses = man.business_set.all()
for i in businesses:
    print(i.business_name,i.man.name)'''

# product = Profile.objects.create(name = 'Sasha',age = 18)
# account = Accoutn.objects.create(nickname = '__panda11__', profile = product)

# profile = Profile.objects.get(id = 1)
# account = Accoutn.objects.get(profile = profile)
# print(account.nickname)
# print(account.profile.name,account.profile.age)

# account = Accoutn.objects.get(id = 1)
# print(account.nickname)
# print(account.profile.name,account.profile.age)

# profile = Profile.objects.all()
# for i in profile:
#     print(i.name,i.age,i.upper_name(),i.check_age())
    
# profile = Profile.objects.get(id = 1)
# print(profile.name,profile.age,profile.upper_name())

# person = Person.objects.annotate(
#     res = F('age')*20
# )
# for i in person:
#     print(i.name,i.age,i.res)

# person = Person.objects.annotate(
#     check = Case(
#         When(age__gte = 18,then=Value('Доросла людина')),
#         default = Value('мала людина'),
#         output_field = CharField()
#     ) 
# )
# for i in person:
#     print(i.name,i.age,i.check)

# abc = Person.objects.create(name = 'Sasha', age = 12, hobby = 'IT')

# all_user = Person.objects.all()
# for i in all_user:
#     print(i.name,i.age)



# try: 
#     person = Person.objects.get(id =1)
#     print(person.name)

# except Person.MultipleObjectsReturned:
#     print("знайдено багато людей ")


# try:
#     person = Person.objects.get(id = 100000)
    
# except Person.DoesNotExist:
#     print('Немає такої людини')

# person = Person.objects.get(id = 2)
# person.delete()

# people = Person.people.check_full_age(18)
# for i in people:
#     print(i.name,i.age)

# people = Person.people.first_person()

# print(people.name,people.age)

people = Person.people.all()

for i in people:
    print(i.name,i.age)