from django.contrib import admin
from django.urls import path, include
from .views import HealthCheckView, LoginView, SignupView

urlpatterns = [
  path('login/', LoginView.as_view()),
  path('signup/', SignupView.as_view()),
  path('health/', HealthCheckView.as_view()),
]
