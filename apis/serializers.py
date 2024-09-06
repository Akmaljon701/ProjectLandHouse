from rest_framework import serializers
from apis import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = [
            'name',
            'phone',
            'email',
            'you_tube',
            'instagram',
            'telegram',
            'facebook',
            'objects_count',
            'clients',
            'years',
            'address',
            'longitude',
            'latitude',
            'description',
        ]


class ObjectPhotosSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = models.ObjectPhoto
        fields = [
            'id',
            'photo'
        ]

    def get_photo(self, obj) -> str:
        if obj.photo:
            return obj.photo.url
        return None


class ObjectRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ObjectRoom
        fields = [
            'id',
            'photo',
            'total_area',
            'block',
            'count',
        ]

    def get_photo(self, obj) -> str:
        if obj.photo:
            return obj.photo.url
        return None


class ObjectsSerializer(serializers.ModelSerializer):
    photos = ObjectPhotosSerializer(many=True)
    rooms = ObjectRoomsSerializer(many=True)
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
            'rooms',
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


class ObjectRoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ObjectRoom
        fields = [
            'id',
            'photo',
            'total_area',
            'block',
            'count',
            'floor',
            'entrance',
            'price',
        ]
