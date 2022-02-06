from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Career
from .serializers import CareerSerializer


class CareerViewSet(ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "author",
    ]


career_list = CareerViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

career_detail = CareerViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
)
