from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'Restaurant Stock Management',
        'name': 'Ghina Nabila Gunawan',
        'class': 'PBP B'
    }
    return render(request, "main.html", context)