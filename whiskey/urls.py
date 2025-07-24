from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 
    path('',views.all_products, name='products'),
    path('create_product/',views.create_product,name='create'),
    path('product_details/<int:id>',views.product_details, name = 'product_details'),
    path('update_product/<int:id>',views.update_product,name = 'update'),
    path('delete_product/<int:id>',views.delete_product,name='delete'),
    # path('test/',views.get_redis_data),
]