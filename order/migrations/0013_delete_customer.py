# Generated by Django 4.1.2 on 2023-03-02 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_rename_pclass_customer_cclass_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='customer',
        ),
    ]
