from rest_framework import serializers
from apis import models


class ObjectPhotosSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = models.ObjectPhoto
        fields = [
            'photo'
        ]

    def get_photo(self, obj) -> str:
        if obj.photo:
            return obj.photo.url
        return None


class ObjectsSerializer(serializers.ModelSerializer):
    photos = ObjectPhotosSerializer(many=True)
    description = serializers.SerializerMethodField()

    class Meta:
        model = models.Object
        fields = [
            'id',
            'title',
            'name',
            'description',
            'status',
            'created_at',
            'photos',
        ]

    def get_description(self, obj) -> str:
        max_length = 20
        description = obj.description
        if len(description) > max_length:
            return description[:max_length] + '...'
        return description


class ObjectDetailSerializer(serializers.ModelSerializer):
    photos = ObjectPhotosSerializer(many=True)

    class Meta:
        model = models.Object
        fields = [
            'id',
            'title',
            'name',
            'description',
            'status',
            'created_at',
            'photos',
        ]
