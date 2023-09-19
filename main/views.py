from django.shortcuts import render
from .models import Item
# new import tugas 3
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    #tambahan kode tugas 3
    items = Item.objects.all()
    num_items = items.count()

    context = {
        'app_name': 'Ghina27-app',
        'my_name': 'Ghina Nabila Gunawan',
        'my_class': 'PBP B',
        'menu_name': 'Sate Pacil',
        'menu_amount': '100',
        'menu_description': 'Ini adalah sate favorit mahasiswa Fasilkom UI',
        'menu_price': '@4.000/tusuk',
        'items': items,
        'num_items': num_items,
    }
    return render(request, "main.html", context)

# tugas 3

# kode di bawah ini untuk menghasilkan formulir yang dapat menambahkan 
# data produk secara otomatis ketika data di-submit dari form.

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")