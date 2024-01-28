from django.urls import path
from .views import *
urlpatterns = [
    path("", NewForm.as_view(), name="Form-new"),
    path("view/", ViewForm.as_view(), name="Form-view"),
    path("update/<int:pk>", UpdateForm.as_view(), name="Form-update"),
    path("delete/<int:pk>", DeleteForm.as_view(), name="Form-delete"),
    path("download/<int:id>/", download, name="download")
]
