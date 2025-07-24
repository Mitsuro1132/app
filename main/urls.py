from django.urls import path, include
from . import views
urlpatterns = [
    path('qweqwrwerwt',views.get,name='hello'),
    path('test/', views.get_request),
    path('text/numb/', views.numb ),
    path('Step/<int:a>/<int:b>/<int:c>/',views.next_step),
    path('string/<str:a>/<str:b>/', views.strok),
    path('hello/',views.templ,name='first'),
    path('stepik',views.step),
    path('key',views.test,name='last'),
    path('datka/',views.test_dict, name= 'text'),
    path('index4/', views.Yulian_gey,),
    path('roma/', views.Roma_warface,),
    path('bbb/',views.view1),
    path('',views.data),
    path('result/',views.post_data,name='result'),
    path('Iphone13/',views.iphone13),
    path('Iphone15/',views.iphone15),
    # path('new/', views.get_new)
]
