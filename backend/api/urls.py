from django.contrib import admin
from django.urls import include, re_path

from api.forms.user_forms import UserAdminForm

from api.routers import \
    album_router,\
    contact_router,\
    comment_router,\
    company_router,\
    cronjob_router,\
    doc_router,\
    email_validation_router,\
    health_router,\
    information_router,\
    location_router,\
    login_router,\
    manufacturer_router,\
    me_router,\
    register_router,\
    state_router,\
    user_router

from core.models.user.user_model import User

admin.site.register(User, UserAdminForm)

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    re_path(r'^albums/', include(album_router.urlpatterns)),
    re_path(r'^contact', include(contact_router.urlpatterns)),
    re_path(r'^comments/', include(comment_router.urlpatterns)),
    re_path(r'^companies/', include(company_router.urlpatterns)),
    re_path(r'^cronjob/', include(cronjob_router.urlpatterns)),
    re_path(r'^docs/', include(doc_router.urlpatterns)),
    re_path(r'^email-validation/', include(email_validation_router.urlpatterns)),
    re_path(r'^health', include(health_router.urlpatterns)),
    re_path(r'^login', include(login_router.urlpatterns)),
    re_path(r'^information/', include(information_router.urlpatterns)),
    re_path(r'^locations/', include(location_router.urlpatterns)),
    re_path(r'^manufacturers/', include(manufacturer_router.urlpatterns)),
    re_path(r'^me', include(me_router.urlpatterns)),
    re_path(r'^register', include(register_router.urlpatterns)),
    re_path(r'^states/', include(state_router.urlpatterns)),
    re_path(r'^users/', include(user_router.urlpatterns)),
]
