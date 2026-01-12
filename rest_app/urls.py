from django.urls import path
from .views.main_view import product_view, product_detail_view

urlpatterns = [
    path('products/', product_view),
    path('products/<int:id>/', product_detail_view),
]