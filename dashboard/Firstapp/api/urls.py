from django.conf.urls import url,include 
from rest_framework import routers 
from Firstapp.api.views import ITJobsCRUDCBV 
router=routers.DefaultRouter() 
router.register('itjobs',ITJobsCRUDCBV) 
urlpatterns = [url('', include(router.urls)),
]
 