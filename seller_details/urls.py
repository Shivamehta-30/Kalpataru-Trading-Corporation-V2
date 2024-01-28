from django.urls import path
from .views import *
urlpatterns = [
    path("new/", NewSeller.as_view(), name="Seller-new"),
    path("view/", ViewSeller.as_view(), name="Seller-view"),
    path("update/<int:pk>", UpdateSeller.as_view(), name="Seller-update"),
    path("delete/<int:pk>", DeleteSeller.as_view(), name="Seller-delete")
]
