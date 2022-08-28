from django.urls import include, path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from dbl import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(title="Inspectorio Test", default_version="v1", description="Test description"),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", include("dblapp.urls")),
    path(
        "api/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
