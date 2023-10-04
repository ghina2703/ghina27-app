from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    # amount = models.IntegerField(default = 10)
    description = models.TextField() 
    # kalau dikasih parameter blank & null itu tidak wajib diisi
    price = models.PositiveIntegerField(default = 20000)
    date_added = models.DateField(auto_now_add=True)
    # === tugas 4
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Tambahkan field amount untuk menyimpan jumlah stok
    amount = models.PositiveIntegerField(default=10)
    # === tugas 5
    # Tambahkan field gambar
    image = models.ImageField(upload_to='item_images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], blank=True, null=True)
