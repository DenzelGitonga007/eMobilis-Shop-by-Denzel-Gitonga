from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('create_product/', views.create_product, name='create_product'), # product creation
    path('list_products/', views.product_list, name='list_products'), # list products
    path('product/<int:pk>/edit/', views.update_product, name='update_product'), # edit product
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'), # delete product
]