# Generated by Django 4.1.2 on 2023-01-08 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_productmodel_pprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pprice',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='pquantity',
            field=models.IntegerField(max_length=30),
        ),
    ]
