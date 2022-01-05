from django.shortcuts import render
from django.http import HttpResponse
from . models import place,blog
# Create your views here.
# def fun(request):
#     obj = place()
#     obj.name = "Kerala"
#     obj.desc = "Gods Own Country"
#     obj.price = 800
#     obj.offer = "Attractive Offer"
#     return render(request, "index.html", {'result': obj})
    #return HttpResponse("Hello Welcome to Travello")
    # return render(request,"home.html",
    #               {'name':'Anees' , 'place':'Hills Gardens, Kozhimala,Ambalappadi,Pallikkara,Ernakulam'})

def fun(request):
    obj = place.objects.all()
    b_obj = blog.objects.all()
    return render(request, "index.html",{'results': obj,'blogs': b_obj})


def addition(request):
    n1=int(request.POST["num1"]) #default type is string, so convert it as int()
    n2=int(request.POST["num2"])
    n3=n1+n2
    return render(request,"result.html", {'add': n3})
