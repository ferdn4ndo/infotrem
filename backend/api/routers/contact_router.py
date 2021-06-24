from django.urls import path

from api.views import ContactView

urlpatterns = [
    path('', ContactView.as_view()),
]
