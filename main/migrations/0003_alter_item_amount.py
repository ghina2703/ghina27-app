# Generated by Django 4.2.5 on 2023-09-25 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_user_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]