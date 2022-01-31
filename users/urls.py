from django.urls import path

from .views import get_csrf_token

urlpatterns = [
    path('/get-csrf', get_csrf_token)
]
