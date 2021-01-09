from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'owner', 'created_at', 'updated_at')
        extra_kwargs = {'owner': {'read_only': True}}