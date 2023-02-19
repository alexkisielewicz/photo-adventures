# Generated by Django 3.2.18 on 2023-02-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230218_2250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('adventure', 'Adventure'), ('travel', 'Travel'), ('nature', 'Nature'), ('landscape', 'Landscape'), ('aerial', 'Aerial'), ('wildlife', 'Wildlife'), ('street', 'Street'), ('architecture', 'Architecture')], default='adventure', max_length=20),
        ),
    ]
