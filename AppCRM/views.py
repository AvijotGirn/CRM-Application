from django.http import JsonResponse
import json
from django.shortcuts import render, HttpResponse, redirect
from .models import Clients

# ----------- Routing
def home(request):
    return render(request, "home.html")

def client_list(request):
    items = Clients.objects.all()
    return render(request, "clients.html", {"client_list": items})

def client_info(request, client):
    return render(request, "clientinfo.html", {"client": Clients.objects.get(id=client)})

def add_client_page(request):
    if request.method == "POST":
        add_client(request)
        return redirect("Clients")
    else:
        return render(request, "add_client.html")

# ----------- DB Manipulation Methods

def update_client_info(request, clientid):
    if request.method == 'POST':
        data = json.loads(request.body)
        updated_data = data.get('updatedData')

        try:
            client = Clients.objects.get(id=clientid)
        except Clients.DoesNotExist:
            return JsonResponse({'error': 'Client not found'}, status=404)

        client.first_name = updated_data.get('clientFirst', client.first_name)
        client.last_name = updated_data.get('clientLast', client.last_name)
        client.email = updated_data.get('email', client.email)
        client.phone = updated_data.get('phone', client.phone)
        client.notes = updated_data.get('notes', client.notes)

        client.save()
        return JsonResponse({'success': 'Client information successfully updated'}, status=200)

    return JsonResponse({'error': 'Invalid Request Method'}, status=400)

# Postman
def add_client(request):

    first_name = request.POST['first']
    last_name = request.POST['last']
    email = request.POST['email']
    phone = request.POST['phone']
    company = request.POST['company']
    notes = request.POST['notes']

    new_client = Clients(first_name=first_name, last_name=last_name, email=email, phone=phone, company=company, notes=notes)
    new_client.save()
    return



