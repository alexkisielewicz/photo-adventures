# Generated by Django 3.2.18 on 2023-02-20 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_keyword'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Keyword',
        ),
    ]