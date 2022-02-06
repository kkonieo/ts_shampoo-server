from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Award
from .serializers import AwardSerializer


class AwardViewSet(ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "author",
    ]


award_list = AwardViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

award_detail = AwardViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
)
