from django.urls import path
from .views import *
urlpatterns = [
    path("new/", NewBuyer.as_view(), name="Buyer-new"),
    path("view/", ViewBuyer.as_view(), name="Buyer-view"),
    path("update/<int:pk>", UpdateBuyer.as_view(), name="Buyer-update"),
    path("delete/<int:pk>", DeleteBuyer.as_view(), name="Buyer-delete")
]
