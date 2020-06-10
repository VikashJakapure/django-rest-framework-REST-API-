from django.contrib import admin
from django.urls import path,re_path,include
from rest_framework import routers
from myapp.views import EmpView,EmpViewAp

router = routers.DefaultRouter()
router.register(r'emp',EmpView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('emp/',EmpViewAp.as_view()),
]
