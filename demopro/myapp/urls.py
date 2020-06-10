from django.urls import path,include
from myapp.views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('stu',TestViewSet,basename='stu')


urlpatterns = [

    path('detalils/',Details.as_view()),
    path('detalils/<str:pk>/', Details.as_view()),
    path('convert/',ConvertView.as_view()),



    # path('info/<str:pk>/', Details.as_view()),



    # path('convert/',TextToAudio.as_view()),
    # path('api/', include(router.urls)),

]
