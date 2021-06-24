from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from api.forms import UserAdmin
from api.models import User
from api.routers import \
    billet_router, \
    billet_gateway_router, \
    contact_router,\
    cronjob_router,\
    doc_router,\
    email_validation_router,\
    event_router,\
    login_router,\
    me_router,\
    register_router,\
    state_router,\
    subscription_eligibility_router,\
    subscription_router,\
    user_router

admin.site.register(User, UserAdmin)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^billet-gateways/', include(billet_gateway_router.urlpatterns)),
    url(r'^billets/', include(billet_router.urlpatterns)),
    url(r'^cronjob/', include(cronjob_router.urlpatterns)),
    url(r'^contact', include(contact_router.urlpatterns)),
    url(r'^docs/', include(doc_router.urlpatterns)),
    url(r'^email-validation/', include(email_validation_router.urlpatterns)),
    url(r'^events/', include(event_router.urlpatterns)),
    url(r'^login', include(login_router.urlpatterns)),
    url(r'^me', include(me_router.urlpatterns)),
    url(r'^register', include(register_router.urlpatterns)),
    url(r'^states/', include(state_router.urlpatterns)),
    url(r'^subscription-eligibility/', include(subscription_eligibility_router.urlpatterns)),
    url(r'^subscriptions/', include(subscription_router.urlpatterns)),
    url(r'^users/', include(user_router.urlpatterns)),
]
