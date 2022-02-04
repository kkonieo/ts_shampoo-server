from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Job
from .serializers import JobSerializer

class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

job_list = JobViewSet.as_view({
    'get': 'list',
    'post': 'create',
})