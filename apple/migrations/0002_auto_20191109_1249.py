# Generated by Django 2.2.6 on 2019-11-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
