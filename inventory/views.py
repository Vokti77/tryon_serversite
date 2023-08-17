# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from inventory.models import Category, Sub_Category
# from inventory.serializers import CategotySerializer, Sub_CategorySerializer

from rest_framework import generics
from .models import Category, Sub_Category, Clothe, Attachment
from .serializers import CategotySerializer, Sub_CategorySerializer, ClothesDetailsSerializer

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


from django.views.generic.edit import FormView
from rest_framework.generics import ListAPIView
from .forms import ClothesForm


class UploadView(FormView):
    template_name = 'upload.html'
    form_class = ClothesForm
    success_url = '/output/'

    def form_valid(self, form):
        attachments = form.cleaned_data['attachments']
        files1 = form.cleaned_data['file1']
        files2 = form.cleaned_data['file2']

        for idx in range(min(len(attachments), len(files1), len(files2))):
            attachment = Clothe.objects.create(
                clothes_orginal=attachments[idx],
                clothes=files1[idx] if idx < len(files1) else None,
                clothes_mask=files2[idx] if idx < len(files2) else None,
            )

        return super(UploadView, self).form_valid(form)
    


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from inventory.serializers import AttachmentSerializer, AttachmentsSerializer, ClothesSerializer

class ClothesViewAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClothesSerializer(data=request.data)

        if serializer.is_valid():
            attachments = serializer.validated_data['attachments']
            files1 = serializer.validated_data.get('file1', [])
            files2 = serializer.validated_data.get('file2', [])

            for idx in range(min(len(attachments), len(files1), len(files2))):
                Clothe.objects.create(
                    clothes_orginal=attachments[idx],
                    clothes=files1[idx] if idx < len(files1) else None,
                    clothes_mask=files2[idx] if idx < len(files2) else None,
                )

            return Response({'message': 'Files uploaded successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClothesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothe.objects.all()
    serializer_class = ClothesDetailsSerializer

class ClothesListView(ListAPIView):
    queryset = Clothe.objects.all()
    serializer_class = ClothesDetailsSerializer


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