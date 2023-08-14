# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from inventory.models import Category, Sub_Category
# from inventory.serializers import CategotySerializer, Sub_CategorySerializer

from rest_framework import generics
from .models import Category, Sub_Category
from .serializers import CategotySerializer, Sub_CategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategotySerializer

class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategotySerializer

class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = Sub_Category.objects.all()
    serializer_class = Sub_CategorySerializer

class SubCategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sub_Category.objects.all()
    serializer_class = Sub_CategorySerializer

# @csrf_exempt
# def categoryApi(request,id=0):
#     if request.method=='GET':
#         categories = Category.objects.all()
#         categories_serializer=CategotySerializer(categories,many=True)
#         return JsonResponse(categories_serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         category_data = JSONParser().parse(request)
#         categories_serializer=Sub_CategorySerializer(data=category_data)

#         if categories_serializer.is_valid():
#             categories_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
    
#     elif request.method == 'PUT':
#         category_data = JSONParser().parse(request)
#         category = Category.objects.get(id=category_data['id'])
#         categories_serializer = CategotySerializer(category, data=category_data)
#         if categories_serializer.is_valid():
#             categories_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")
    
#     elif request.method ==' DELETE':
#         category=Category.objects.get(id=id)
#         category.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

from django.shortcuts import render, redirect
from .models import Image, Attachment

def upload_images(request):
    if request.method == 'POST':
        image_names = request.POST.getlist('image_name[]')
        image_originals = request.FILES.getlist('image_originals[]')
        image_clothes = request.FILES.getlist('image_clothes[]')
        image_masks = request.FILES.getlist('image_masks[]')

        for name, orig, clothes, mask in zip(image_names, image_originals, image_clothes, image_masks):
            image = Image(
                image_name=name,
                image_originals=orig,
                image_clothes=clothes,
                image_masks=mask
            )
            image.save()

        return redirect('output')

    return render(request, 'upload.html')

def output(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'output.html', context)


from django.shortcuts import render, redirect
from .forms import ImageForm

def upload_images(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = ImageForm()
    
    context = {'form': form}
    return render(request, 'upload.html', context)


from django.views.generic.edit import FormView
from rest_framework.generics import ListAPIView
from .forms import UploadForm
from .models import Product

class UploadView(FormView):
    template_name = 'upload.html'
    form_class = UploadForm
    success_url = '/output/'

    def form_valid(self, form):
        attachments = form.cleaned_data['attachments']
        files1 = form.cleaned_data['file1']
        files2 = form.cleaned_data['file2']

        for idx in range(min(len(attachments), len(files1), len(files2))):
            attachment = Attachment.objects.create(
                file=attachments[idx],
                file1=files1[idx] if idx < len(files1) else None,
                file2=files2[idx] if idx < len(files2) else None,
            )

        return super(UploadView, self).form_valid(form)
    
    # def form_valid(self, form):
    #     attachments = form.cleaned_data['attachments']
    #     files1 = form.cleaned_data['file1']
    #     files2 = form.cleaned_data['file2']

    #     for each in attachments:
    #         attachment = Attachment.objects.create(file=each)

    #     for file1 in files1:
    #         Attachment.objects.create(file1=file1)

    #     for file2 in files2:
    #         Attachment.objects.create(file2=file2)

    #     return super(UploadView, self).form_valid(form)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from inventory.serializers import AttachmentSerializer, AttachmentsSerializer

class UploadViewAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AttachmentSerializer(data=request.data)

        if serializer.is_valid():
            attachments = serializer.validated_data['attachments']
            files1 = serializer.validated_data.get('file1', [])
            files2 = serializer.validated_data.get('file2', [])

            for idx in range(min(len(attachments), len(files1), len(files2))):
                Attachment.objects.create(
                    file=attachments[idx],
                    file1=files1[idx] if idx < len(files1) else None,
                    file2=files2[idx] if idx < len(files2) else None,
                )

            return Response({'message': 'Files uploaded successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttachmentListView(ListAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentsSerializer