from django.urls import path
from authapp.views import Access,Details
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('auth-token',ObtainAuthToken.as_view()),
    path('access',Access.as_view()),
    path('details',Details.as_view()),

]