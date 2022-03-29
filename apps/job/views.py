from rest_framework.generics import ListAPIView
from .models import Job
from .serializers import JobSerializer


class JobListAPIView(ListAPIView):
    """
    직군 리스트
    """

    queryset = Job.objects.all()
    serializer_class = JobSerializer