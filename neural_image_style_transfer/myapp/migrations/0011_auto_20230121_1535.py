# Generated by Django 3.2.16 on 2023-01-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20230121_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='image2',
        ),
        migrations.AlterField(
            model_name='upload',
            name='image1',
            field=models.FileField(upload_to='myapp/input'),
        ),
    ]
