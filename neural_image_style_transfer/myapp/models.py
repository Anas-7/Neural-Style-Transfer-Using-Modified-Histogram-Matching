from django.db import models

class Upload(models.Model):
    title=models.CharField(max_length=50)
    image1=models.ImageField(upload_to="myapp/input")
    image2=models.ImageField(upload_to="myapp/input")
    final_image=models.ImageField(upload_to="myapp/output", null=True)
