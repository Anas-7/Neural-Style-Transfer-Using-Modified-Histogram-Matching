from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import UploadForm
from django.shortcuts import redirect
from .neural_style_transfer_using_modified_histogram_matching import LoadImages, InputImagePreprocessing, NST
from .models import Upload
# Create your views here.

def home(request):
    flag=False
    upload=None
    if request.method=='POST':
        form=UploadForm(request.POST,request.FILES)
        if form.is_valid():
            upload=form.save()
            content_image, style_image = LoadImages(content_image_name = str(form.cleaned_data.get("image1")),
                                          style_image_name = str(form.cleaned_data.get("image2"))).load()
            input_image_preprocessor = InputImagePreprocessing()
            
            input_image = input_image_preprocessor.preprocess(content_image, style_image)
            STYLE_LAYERS = [
            ('block1_conv1', 0.2),
            ('block2_conv1', 0.2),
            ('block3_conv1', 0.2),
            ('block4_conv1', 0.2),
            ("block5_conv1",0.2)]
            CONTENT_LAYERS = [
            ("block4_conv1",1)]
            nst = NST(input_image, str(form.cleaned_data.get("image1")), content_image,
                     str(form.cleaned_data.get("image2")), style_image, STYLE_LAYERS, CONTENT_LAYERS)
            image_name=nst.single_mode()
            flag=True
            upload.final_image=image_name
            upload.save()           
        else:
            print("invalid")
    else:
        form=UploadForm()
    return render(request, 'myapp/home.html',{'form':form,'flag':flag,'upload':upload})