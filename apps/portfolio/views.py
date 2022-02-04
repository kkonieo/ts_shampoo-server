from django.forms import ValidationError
from django.shortcuts import redirect, render
from rest_framework import generics

from apps.portfolio import serializers

from .models import Project
from .serializers import ProjectDetailSerializer, ProjectSerializer

# Create your views here.


class ProjectAPI(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(author_id=self.kwargs['author'])

    def perform_create(self, serializer):
        serializer.save()


class ProjectDetailAPI(generics.ListCreateAPIView):
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.filter(id=self.kwargs['pk'])


class ProjectDeleteAPI(generics.ListCreateAPIView):
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        target = Project.objects.filter(id=self.kwargs['pk'])
        target.delete()


class ProjectUpdateAPI(generics.ListCreateAPIView):
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.filter(id=self.kwargs['pk'])

    def update(self, serializer):
        try:
            serializer.update()
        except ValidationError as e:
            print(e.message)
