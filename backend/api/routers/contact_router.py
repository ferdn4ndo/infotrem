from django.urls import path

from api.views.contact.contact_view import ContactView

urlpatterns = [
    path('', ContactView.as_view()),
]
