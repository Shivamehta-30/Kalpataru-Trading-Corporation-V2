from django.urls import path
from .views import *
urlpatterns = [
    path("new/", NewAgent.as_view(), name="Agent-new"),
    path("view/", ViewAgent.as_view(), name="Agent-view"),
    path("update/<int:pk>", UpdateAgent.as_view(), name="Agent-update"),
    path("delete/<int:pk>", DeleteAgent.as_view(), name="Agent-delete")
]
