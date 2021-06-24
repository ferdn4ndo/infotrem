from django.urls import path

from api.views import SubscriptionEligibilityView

urlpatterns = [
    path('check', SubscriptionEligibilityView.as_view()),
]
