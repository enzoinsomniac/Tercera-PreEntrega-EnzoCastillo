# Generated by Django 5.1.3 on 2024-11-25 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppE', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitarra',
            name='marca',
            field=models.CharField(max_length=40),
        ),
    ]
