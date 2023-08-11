from django.urls import re_path

from api.views.doc.doc_view import docs_schema_view

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', docs_schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', docs_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', docs_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
