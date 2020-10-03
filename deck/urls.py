from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.probability_of_card, name="card")
]
