# Generated by Django 3.2.16 on 2023-01-21 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_upload2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='final_image',
            field=models.FileField(upload_to='myapp/output'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='image1',
            field=models.FileField(upload_to='myapp/input'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='image2',
            field=models.FileField(upload_to='myapp/input'),
        ),
        migrations.AlterField(
            model_name='upload2',
            name='final_image',
            field=models.FileField(upload_to='myapp/output'),
        ),
        migrations.AlterField(
            model_name='upload2',
            name='image1',
            field=models.FileField(upload_to='myapp/input'),
        ),
        migrations.AlterField(
            model_name='upload2',
            name='image2',
            field=models.FileField(upload_to='myapp/input'),
        ),
    ]
