from django.http import JsonResponse
import json
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