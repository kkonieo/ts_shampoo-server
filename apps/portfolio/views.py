from django.shortcuts import render
from .models import Project
from .serializers import ProjectSerializer, ProjectDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from knox.auth import TokenAuthentication
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class ProjectAPI(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class ProjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]