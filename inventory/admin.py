from django.contrib import admin
from inventory.models import Category, Sub_Category, Attachment, Image, Product


# class ProductAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Product._meta.fields]
#     form = ProductModelForm

# admin.site.register(Product, ProductAdmin)


admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Image)
admin.site.register(Attachment)