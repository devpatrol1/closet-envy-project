# Generated by Django 4.2.5 on 2023-10-05 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='zipcode',
            new_name='zip_code',
        ),
    ]
