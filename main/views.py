from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'ghina2703',
        'my_name': 'Ghina Nabila Gunawan',
        'my_class': 'PBP B'
    }
    return render(request, "main.html", context)