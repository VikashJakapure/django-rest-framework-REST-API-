from rest_framework import viewsets 
from Firstapp.models import ITJobs
from Firstapp.api.serializers import ITJobsSerializer 
class ITJobsCRUDCBV(viewsets.ModelViewSet):
    serializer_class=ITJobsSerializer 
    queryset=ITJobs.objects.all()
