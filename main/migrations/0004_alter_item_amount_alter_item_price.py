# Generated by Django 4.2.5 on 2023-09-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_item_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=20000),
        ),
    ]