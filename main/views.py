from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
# new import tugas 3 dan 4
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
# new impor tugas 5
from django.db.models import Q


# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    search_query = request.GET.get('search', '')  # Mendapatkan parameter pencarian dari query string
    items = Item.objects.filter(user=request.user)
    num_items = items.count()
    last_login = request.COOKIES['last_login']

    # Mencari daftar produk berdasarkan nama atau deskripsi yang cocok dengan query pencarian
    items = items.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    context = {
        'app_name': 'Ghina27-app',
        'my_name': request.user.username,
        'my_class': 'PBP B',
        'items': items,
        'num_items': num_items,
        'last_login': last_login,
    }
    return render(request, "main.html", context)

# ========= tugas 3

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES) # Menggunakan request.FILES untuk menangani file gambar
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('main:show_main')
    else:
        form = ItemForm()

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# ======== tugas 4

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_item(request, id):
    item = get_object_or_404(Item, pk=id)

    if item.amount >= 0:  # Tambahkan pengecekan stok tidak kurang dari 0
        item.amount += 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def reduce_item(request, id):
    item = get_object_or_404(Item, pk=id)

    if item.amount > 0: # Tambahkan pengecekan stok tidak kurang dari 1
        item.amount -= 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_item(request, id):
    # Get data berdasarkan ID
    item = Item.objects.get(pk = id)
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item) # Menggunakan request.FILES untuk menangani file gambar
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    else:
        form = ItemForm(instance=item)
    
    context = {'form': form, 'item': item}
    return render(request, "edit_item.html", context)