from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .form import ClientForm

def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

def new_client(request):
    form = ClientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(list_clients)

    return render(request, 'form.html', {'form':form})

def update_client(request, id):
    client = get_object_or_404(Client, pk=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect(list_clients)

    return render(request, 'form.html', {'form':form})

def delete_client(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == 'POST':
        client.delete()
        return redirect(list_clients)

    return render(request, 'confirm.html', {'client':client})