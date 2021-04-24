# Generated by Django 3.2 on 2021-04-23 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0002_auto_20210423_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetail',
            name='institution',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact_details', to='institutions.institution'),
            preserve_default=False,
        ),
    ]
