from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.services.docs_schema_generator.docs_schema_generator_service import DocsSchemaGeneratorService

docs_schema_view = get_schema_view(
   openapi.Info(
      title="Infotrem API",
      default_version='v1',
      description="Railroad information and media management API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="const.fernando@gmail.com"),
      license=openapi.License(name="MIT License"),
      url="https://api.infotrem.com.br/",
   ),
   generator_class=DocsSchemaGeneratorService,
   public=True,
   permission_classes=[permissions.AllowAny],
)
