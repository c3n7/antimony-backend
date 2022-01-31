from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware.csrf import get_token


@api_view()
def get_csrf_token(request):
    token = get_token(request)
    response = Response({'csrfToken': token})
    response["X-CSRFToken"] = token
    return response
