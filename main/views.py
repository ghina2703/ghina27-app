from django.shortcuts import render
from .models import Item
# Create your views here.
def show_main(request):
    context = {
        'app_name': 'ghina27-app',
        'my_name': 'Ghina Nabila Gunawan',
        'my_class': 'PBP B',
        'item': Item.objects.all(),
    }
    return render(request, "main.html", context)