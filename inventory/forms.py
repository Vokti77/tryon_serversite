import json
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django import forms
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField
from .models import ImageModel, Product

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ('clothes', 'original', 'mask')

class UploadForm(forms.Form):
    name = forms.CharField(max_length=100)
    attachments = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)
    file1 = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)
    file2 = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)
