from django.urls import path,include
from myapp.views import *
from rest_framework import routers


urlpatterns = [
    path('test/',QueryParams.as_view()),
    path('stu/',StudentGenericViewSet.as_view()),
    path('stu/<str:pk>/', StudentGenericViewSet.as_view()),

]
