from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.views import APIView
from apis import models, serializers
from utils.languages import language
from utils.pagination import PaginationDynamicResponseSerializer, paginate_dynamic
from apis.exceptions import error_exception, ErrorCodes
from rest_framework import exceptions
from rest_framework.response import Response


class ObjectsAPIView(APIView):
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

        lang = request.headers.get('lang', 'uz')
        language(lang)

        objects = models.Object.objects.all().order_by('-created_at')

        return paginate_dynamic(objects, serializers.ObjectsSerializer, request, page, limit)


class ObjectAPIView(APIView):
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
