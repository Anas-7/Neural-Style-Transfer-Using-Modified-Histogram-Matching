# Generated by Django 3.2.16 on 2023-01-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_upload_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='image1',
            field=models.ImageField(upload_to='myapp/input'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='image2',
            field=models.ImageField(upload_to='myapp/input'),
        ),
    ]
