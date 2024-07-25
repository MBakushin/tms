from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet


# API Schema
schema_view = get_schema_view(openapi.Info(
    title="TSM API",
    default_version='v1',
    description="TSM API",),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]
