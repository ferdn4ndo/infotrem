from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from api.forms.user_forms import UserAdminForm

from api.routers import \
    album_router,\
    contact_router,\
    comment_router,\
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
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^albums/', include(album_router.urlpatterns)),
    url(r'^cronjob/', include(cronjob_router.urlpatterns)),
    url(r'^contact', include(contact_router.urlpatterns)),
    url(r'^comments/', include(comment_router.urlpatterns)),
    url(r'^docs/', include(doc_router.urlpatterns)),
    url(r'^email-validation/', include(email_validation_router.urlpatterns)),
    url(r'^health', include(health_router.urlpatterns)),
    url(r'^login', include(login_router.urlpatterns)),
    url(r'^information/', include(information_router.urlpatterns)),
    url(r'^locations/', include(location_router.urlpatterns)),
    url(r'^manufacturers/', include(manufacturer_router.urlpatterns)),
    url(r'^me', include(me_router.urlpatterns)),
    url(r'^register', include(register_router.urlpatterns)),
    url(r'^states/', include(state_router.urlpatterns)),
    url(r'^users/', include(user_router.urlpatterns)),
]
