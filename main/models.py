from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField() 
    # kalau dikasih parameter blank & null itu tidak wajib diisi
    price = models.IntegerField(default = 20000)
    date_added = models.DateField(auto_now_add=True)