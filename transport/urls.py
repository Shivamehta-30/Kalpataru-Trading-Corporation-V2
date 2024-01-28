from django.urls import path
from .views import *
urlpatterns = [
    path("new/", NewTransport.as_view(), name="Transport-new"),
    path("view/", NewTransport.as_view(), name="Transport-view"),
    path("update/<int:pk>", NewTransport.as_view(), name="Transport-update"),
    path("delete/<int:pk>", NewTransport.as_view(), name="Transport-delete")
]
