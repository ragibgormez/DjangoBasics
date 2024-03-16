from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("<int:categoryId>", views.getProductsByCategoryId,),
    path("<str:category>", views.getProductsByCategory, name="productsByCategori"),
   # path("<deneme>", views.denemeFonk, name="details")vdfbd
    
]
