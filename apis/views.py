from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.views import APIView
from apis import models, serializers
from utils.languages import language
from utils.pagination import PaginationDynamicResponseSerializer, paginate_dynamic
from apis.exceptions import error_exception, ErrorCodes
from rest_framework import exceptions
from rest_framework.response import Response


class BaseAPIView(APIView):
    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)

        lang = request.headers.get('lang', 'uz')
        language(lang)

        return request


class CompanyAPIView(BaseAPIView):
    @extend_schema(
        summary="Company statistics",
        request=None,
        responses=serializers.CompanySerializer,
    )
    def get(self, request):
        company = models.Company.objects.first()
        ser = serializers.CompanySerializer(company)
        return Response(ser.data, 200)


class ObjectsAPIView(BaseAPIView):
    @extend_schema(
        summary="Objects",
        request=None,
        responses=PaginationDynamicResponseSerializer(child_serializer_class=serializers.ObjectsSerializer),
        parameters=[
            OpenApiParameter(name='page', required=True, type=OpenApiTypes.INT),
            OpenApiParameter(name='limit', required=True, type=OpenApiTypes.INT),
        ]
    )
    def get(self, request):
        page = request.query_params.get('page')
        limit = request.query_params.get('limit')

        objects = models.Object.objects.all().order_by('-created_at')

        return paginate_dynamic(objects, serializers.ObjectsSerializer, request, page, limit)


class ObjectAPIView(BaseAPIView):
    @extend_schema(
        summary="Object",
        request=None,
        responses=serializers.ObjectDetailSerializer,
        parameters=[
            OpenApiParameter(name="pk", description="Object ID", type=OpenApiTypes.INT, required=True)
        ]
    )
    def get(self, request):
        pk = request.query_params.get('pk')

        try:
            obj = models.Object.objects.get(id=pk)
        except models.Object.DoesNotExist:
            raise error_exception(
                exceptions.NotFound,
                ErrorCodes.OBJECT_NOT_FOUND
            )

        ser = serializers.ObjectDetailSerializer(obj)

        return Response(ser.data, 200)


class ObjectRoomAPIView(BaseAPIView):
    @extend_schema(
        summary="Room",
        request=None,
        responses=serializers.ObjectRoomDetailSerializer,
        parameters=[
            OpenApiParameter(name="pk", description="Room ID", type=OpenApiTypes.INT, required=True)
        ]
    )
    def get(self, request):
        pk = request.query_params.get('pk')

        try:
            room = models.ObjectRoom.objects.get(id=pk)
        except models.ObjectRoom.DoesNotExist:
            raise error_exception(
                exceptions.NotFound,
                ErrorCodes.ROOM_NOT_FOUND
            )
        ser = serializers.ObjectRoomDetailSerializer(room)
        return Response(ser.data, 200)
