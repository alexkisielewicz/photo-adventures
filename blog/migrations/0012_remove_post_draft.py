# Generated by Django 3.2.18 on 2023-02-26 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_draft'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='draft',
        ),
    ]