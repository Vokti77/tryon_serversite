from inventory.models import Category, Sub_Category, Clothe
from rest_framework import serializers

class Sub_CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Sub_Category 
        # fields = '__all__'
        fields = ('name', 'category', 'category_name', 'create_at', 'update_at')

class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'


class ClothesSerializer(serializers.Serializer):
    # sub_category = Sub_CategorySerializer()
    # category = CategotySerializer()

    image1 = serializers.ListField(child=serializers.FileField())
    image2 = serializers.ListField(child=serializers.FileField(), required=False)
    image3 = serializers.ListField(child=serializers.FileField(), required=False)

    class Meta:
        model = Clothe
        fields = '__all__'



        
class ClothesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothe
        # fields = ('sleeve', 'lenth', 'ckpt', 'category', 'sub_category' )
        fields = '__all__'

