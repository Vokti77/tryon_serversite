import json
from django.db import models
import os

class Category(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)   # T-Shirt
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Short sleeve 
    id   = models.AutoField(primary_key=True, null=False, unique=True)
    category = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    image_name = models.CharField(max_length=100, blank=True)
    image_originals = models.FileField(upload_to='images/originals/')
    image_clothes = models.FileField(upload_to='images/clothes/')
    image_masks = models.FileField(upload_to='images/masks/')

    def save(self, *args, **kwargs):
        if not self.image_name:  
            base_name = os.path.basename(self.image_originals.name)
            name, extension = os.path.splitext(base_name)
            self.image_name = name
        super(Image, self).save(*args, **kwargs)


    def __str__(self):
        return self.image_name

from django.db import models

class ImageModel(models.Model):
    clothes = models.ImageField(upload_to='images/')
    original = models.ImageField(upload_to='images/')
    mask = models.ImageField(upload_to='images/')
    # You can add more fields if needed
    
    def __str__(self):
        return f"Image Model {self.pk}"
    

class Product(models.Model):
    #your other fields
    multiview_images = models.TextField(blank=True,null=True) 

    def get_multiview_images_list(self):
        if self.multiview_images:
            try:
                urls = json.loads(self.multiview_images)
                return [ {url} for url in urls]
            except json.JSONDecodeError as e:
                print("JSON Decode Error:", e)
        return []

    def set_multiview_images(self, images):
        self.multiview_images = json.dumps(images)
        
        

class Attachment(models.Model):
    image_name = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='attachments')
    file1 = models.FileField(upload_to='attachments1', default='')
    file2 = models.FileField(upload_to='attachments2', default='')

    def save(self, *args, **kwargs):
        if not self.image_name:  
            base_name = os.path.basename(self.file.name)
            name, extension = os.path.splitext(base_name)
            self.image_name = name
        super(Attachment, self).save(*args, **kwargs)
        

# class Clothe(models.Model):
#     category = models.CharField(max_length=50)
#     sub_category = models.CharField(max_length=50)
#     clothe_name = models.CharField(max_length=50, blank=True)

#     SLEEVE_CHOICES = [
#         ("full", "full"),
#         ("half", "half"),
        
#     ]
#     sleeve = models.CharField(max_length=5, choices=SLEEVE_CHOICES, default="full")

#     LENTH_CHOICES = [
#         ("full", "full"),
#         ("half", "half"),
        
#     ]
#     lenth = models.CharField(max_length=5, choices=LENTH_CHOICES, default="full")

#     CKPT_CHOICES = [
#         ("0", "0"),
#         ("1", "1"),
        
#     ]
#     ckpt = models.CharField(max_length=5, choices=CKPT_CHOICES, default="0")
#     clothes_orginal = ArrayField(models.CharField(max_length=100), blank=True)
#     clothes = ArrayField(models.CharField(max_length=100), blank=True)
#     clothes_mask = ArrayField(models.CharField(max_length=100), blank=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)

#     # def save(self, *args, **kwargs):
#     #     if not self.clothe_name:  
#     #         base_name = os.path.basename(self.clothes_orginal.name)
#     #         name, extension = os.path.splitext(base_name)
#     #         self.clothe_name = name
#     #     super(Clothe, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.clothe_name


        
#     def __str__(self):
#         return self.image_name
    
#     def save(self, *args, **kwargs):
#         if not self.image_name:
#             base_name = os.path.basename(self.image_orginal.name)
#             name, extension = os.path.splitext(base_name)
#             self.image_name = name
            
#         super(Clothe, self).save(*args, **kwargs)

#         for index, image_name in enumerate([self.image_orginal.name, self.image.name, self.image_mask.name]):
#             image_instance = ClotheImage.objects.create(
#                 clothe=self,
#                 image_orginal=self.image_orginal,
#                 image=self.image,
#                 image_mask=self.image_mask,
#                 image_name=f"{self.image_name}_{index+1}"
#             )
