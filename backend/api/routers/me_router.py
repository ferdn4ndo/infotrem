from django.urls import path

from api.views.me.me_view import MeView

urlpatterns = [
    path('', MeView.as_view()),
]
