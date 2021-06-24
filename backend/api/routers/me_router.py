from django.urls import path

from api.views import MeView

urlpatterns = [
    path('', MeView.as_view()),
]
