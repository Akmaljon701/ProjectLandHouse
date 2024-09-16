from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.views import APIView
from apis import models, serializers
from utils.languages import language
from utils.pagination import PaginationDynamicResponseSerializer, paginate_dynamic
from apis.exceptions import error_exception, ErrorCodes
from rest_framework import exceptions
from rest_framework.response import Response
from utils.responses import success, response_schema


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

        objects = models.Object.objects.all().prefetch_related('photos').order_by('-created_at')

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
            obj = models.Object.objects.prefetch_related('photos', 'rooms').get(id=pk)
        except models.Object.DoesNotExist:
            raise error_exception(
                exceptions.NotFound,
                ErrorCodes.OBJECT_NOT_FOUND
            )

        ser = serializers.ObjectDetailSerializer(obj)

        return Response(ser.data, 200)


class ObjectMainAPIView(BaseAPIView):
    @extend_schema(
        summary="Object main",
        request=None,
        responses=serializers.ObjectDetailSerializer,
    )
    def get(self, request):

        obj = models.Object.objects.filter(main=True).last()
        if not obj:
            obj = models.Object.objects.all().last()

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


class ApplicationsAPIView(APIView):
    @extend_schema(
        summary="Create Application",
        request=serializers.ApplicationCreateSerializer,
        responses=response_schema
    )
    def post(self, request):
        ser = serializers.ApplicationCreateSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return success


class NewsAPIView(BaseAPIView):
    @extend_schema(
        summary="News",
        request=None,
        responses=PaginationDynamicResponseSerializer(child_serializer_class=serializers.NewsSerializer),
        parameters=[
            OpenApiParameter(name='page', required=True, type=OpenApiTypes.INT),
            OpenApiParameter(name='limit', required=True, type=OpenApiTypes.INT),
        ]
    )
    def get(self, request):
        page = request.query_params.get('page')
        limit = request.query_params.get('limit')

        news = models.New.objects.all().order_by('-id')

        return paginate_dynamic(news, serializers.NewsSerializer, request, page, limit)


class NewAPIView(BaseAPIView):
    @extend_schema(
        summary="New",
        request=None,
        responses=serializers.NewDetailSerializer,
        parameters=[
            OpenApiParameter(name="pk", description="New ID", type=OpenApiTypes.INT, required=True)
        ]
    )
    def get(self, request):
        pk = request.query_params.get('pk')

        try:
            new = models.New.objects.get(id=pk)
        except models.New.DoesNotExist:
            raise error_exception(
                exceptions.NotFound,
                ErrorCodes.NEW_NOT_FOUND
            )

        ser = serializers.NewDetailSerializer(new)

        return Response(ser.data, 200)
