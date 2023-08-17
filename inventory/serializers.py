from inventory.models import Category, Sub_Category, Attachment, Clothe
from rest_framework import serializers

class Sub_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category 
        fields = '__all__'

class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'


class ClothesSerializer(serializers.Serializer):
    attachments = serializers.ListField(child=serializers.FileField())
    file1 = serializers.ListField(child=serializers.FileField(), required=False)
    file2 = serializers.ListField(child=serializers.FileField(), required=False)

    class Meta:
        model = Clothe
        fields = '__all__'

class ClothesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothe
        # fields = ('sleeve', 'lenth', 'ckpt', 'category', 'sub_category' )
        fields = '__all__'

class AttachmentSerializer(serializers.Serializer):
    attachments = serializers.ListField(child=serializers.FileField())
    file1 = serializers.ListField(child=serializers.FileField(), required=False)
    file2 = serializers.ListField(child=serializers.FileField(), required=False)


class AttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'