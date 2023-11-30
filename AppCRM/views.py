from django.shortcuts import render, HttpResponse
from .models import Customers


# Create your views here.
def home(request):
    return render(request, "home.html")

def cust_list(request):
    items = Customers.objects.all()
    return render(request, "customers.html", {"cust_list": items})

def cust_notes(request):
    return render(request, "custinfo.html", {"cust": request.POST.get("hidden","")})
