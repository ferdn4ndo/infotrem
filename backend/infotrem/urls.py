"""infotrem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from infotrem.views import login, media, users, files

from infotrem.routers import information_router, location_router, manufacturer_router, railroad_company_router, \
    railroad_route_router

admin.autodiscover()

urlpatterns = [
    #https://jpadilla.github.io/django-rest-framework-jwt/
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),

    path('admin/', admin.site.urls),
    #path('setup-db', setup.run_from_request, name='setup-db'),
    path('login', login.PerformLogin.as_view(), name='login'),
    path('media/upload/', media.UploadMedia.as_view(), name='media.upload'),
    path('storage/files', files.ListUploadedFiles.as_view(), name='storage.files'),
    path('media/', media.MediaItemListView.as_view(), name='media'),
    path('media/<str:media_uuid>/rolling_stock', media.MediaItemRollingStockView.as_view(), name='media.rollingstock'),
    path('admin-users/', users.AdminListUsers.as_view(), name='users'),
    path('users/', users.UserList.as_view()),
    path('users/<int:pk>/', users.UserDetail.as_view()),

    url(r'^information/', include(information_router.router.urls)),
    url(r'^locations/', include(location_router.router.urls)),
    url(r'^manufacturers/', include(manufacturer_router.router.urls)),
    url(r'^railroad-company/', include(railroad_company_router.router.urls)),
    url(r'^railroad-route/', include(railroad_route_router.router.urls)),
]


