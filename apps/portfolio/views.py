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
        try:
            return Project.objects.filter(author_id=self.kwargs['author'])
        except BaseException as e:
            print(e.message)

    def perform_create(self, serializer):
        serializer.save()


class ProjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        try:
            return Project.objects.filter(author_id=self.kwargs['author'], id=self.kwargs['pk'])  # noqa : W503
        except BaseException as e:
            print(e.message)
