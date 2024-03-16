
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
import datetime


data = {
    "telefon": ["samsung s20", "samsung s21", "Iphone14"], 
    "bilgisayar": ["laptop 1", "laptop 2"],
    "elektronik": []

}

def index(request):
    categories = list(data.keys())
    return render(request, "index.html", {
        "categories": categories
    })


def getProductsByCategoryId(request, categoryId):
    categoryList = list(data.keys())
    if categoryId > len(categoryList):
        return HttpResponseNotFound("yanlış kategori seçimi")
    
    categoryName = categoryList[categoryId-1]
    redirectPath = reverse("productsByCategori", args=[categoryName]) 

    return redirect(redirectPath)
    #return HttpResponseRedirect("/products/telefon")

def getProductsByCategory(request, category):
    try:
        products = data[category]
        return render(request, "products.html", {
            "category": category,
            "products": products,
            "now": datetime.datetime.now(),
        })
    except:
        return HttpResponseNotFound(f"<h1>yanlış kategori seçimi<h1>")
    
#def denemeFonk(request, deneme):
 #   return HttpResponse("ggg")
