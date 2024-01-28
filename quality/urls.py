from django.urls import path
from .views import *
urlpatterns = [
    path("new/", NewQuality.as_view(), name="Quality-new"),
    path("view/", ViewQuality.as_view(), name="Quality-view"),
    path("update/<int:pk>", UpdateQuality.as_view(), name="Quality-update"),
    path("delete/<int:pk>", DeleteQuality.as_view(), name="Quality-delete")
]
