from django.shortcuts import render
from .models import Item
# Create your views here.
def show_main(request):
    context = {
        'app_name': 'Ghina27-app',
        'my_name': 'Ghina Nabila Gunawan',
        'my_class': 'PBP B',
        'menu_name': 'Sate Pacil',
        'menu_amount': '100',
        'menu_description': 'Ini adalah sate favorit mahasiswa Fasilkom UI',
        'menu_price': '@4.000/tusuk',
        'item': Item.objects.all(),
    }
    return render(request, "main.html", context)