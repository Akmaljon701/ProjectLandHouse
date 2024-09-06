from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from apis import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('companies/', views.CompanyAPIView.as_view()),

    path('applications/', views.ApplicationsAPIView.as_view()),

    path('objects/', views.ObjectsAPIView.as_view()),
    path('objects/object/', views.ObjectAPIView.as_view()),
    path('objects/object/room/', views.ObjectRoomAPIView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
