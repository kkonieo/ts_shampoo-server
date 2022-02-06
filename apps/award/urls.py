from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.award_list),
    path("<int:pk>/", views.award_detail),
]
