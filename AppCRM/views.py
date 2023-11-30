from django.shortcuts import render, HttpResponse
from .models import Clients

# Create your views here.
def home(request):
    return render(request, "home.html")

def client_list(request):
    items = Clients.objects.all()
    return render(request, "clients.html", {"client_list": items})

def client_info(request, client):
    return render(request, "clientinfo.html", {"client": Clients.objects.get(id=client)})
