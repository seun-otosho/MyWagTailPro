# Generated by Django 3.2 on 2021-04-23 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0005_alter_contactcategory_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='address',
            table='addresses',
        ),
    ]