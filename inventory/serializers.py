from inventory.models import Category, Sub_Category, Attachment
from rest_framework import serializers

class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ('id','name', 'create_at', 'update_at')

class Sub_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category 
        fields = ('id','name', 'create_at', 'update_at')


class AttachmentSerializer(serializers.Serializer):
    attachments = serializers.ListField(child=serializers.FileField())
    file1 = serializers.ListField(child=serializers.FileField(), required=False)
    file2 = serializers.ListField(child=serializers.FileField(), required=False)


class AttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'