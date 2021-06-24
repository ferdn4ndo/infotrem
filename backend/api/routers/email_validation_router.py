from django.urls import path

from api.views import EmailValidationCheckView, EmailValidationResendView

urlpatterns = [
    path('check/<slug:user_id>/<slug:validation_hash>/', EmailValidationCheckView.as_view()),
    path('resend/', EmailValidationResendView.as_view())
]
