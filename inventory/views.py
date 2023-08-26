from rest_framework import generics
from .models import Category, Sub_Category, Clothe
from .serializers import CategotySerializer, Sub_CategorySerializer, ClothesDetailsSerializer, ClothesSerializer
from django.views.generic.edit import FormView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView


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


class ClothesViewAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClothesSerializer(data=request.data)

        if serializer.is_valid():
            # sub_category_data = serializer.validated_data.pop('sub_category')
            # category_data = serializer.validated_data.pop('category')

            # sub_category_instance, _ = Sub_Category.objects.get_or_create(**sub_category_data)
            # category_instance, _ = Category.objects.get_or_create(**category_data)

            image1 = serializer.validated_data['image1']
            image2 = serializer.validated_data.get('image2', [])
            image3 = serializer.validated_data.get('image3', [])

            for idx in range(min(len(image1), len(image2), len(image3))):
                Clothe.objects.create(
                    # sub_category=sub_category_instance,
                    # category=category_instance,
                    clothes_orginal=image1[idx],
                    clothes=image2[idx] if idx < len(image2) else None,
                    clothes_mask=image3[idx] if idx < len(image3) else None,
                )

            return Response({'message': 'Files uploaded successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClothesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothe.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PATCH' or self.request.method == 'PUT':
            return ClothesDetailsSerializer
        return ClothesDetailsSerializer


class ClothesListView(ListAPIView):
    queryset = Clothe.objects.all()
    serializer_class = ClothesDetailsSerializer


