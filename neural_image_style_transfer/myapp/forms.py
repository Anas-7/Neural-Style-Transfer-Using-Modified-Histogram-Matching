from django import forms
from .models import Upload
from myapp.views import *
class UploadForm(forms.ModelForm):
    class Meta:
        model=Upload 
        fields=['title','image1','image2']