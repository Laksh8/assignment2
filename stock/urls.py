from django.urls import path

from . import views

urlpatterns = [
        path("", views.StockManager.as_view(), name="stock")
]
