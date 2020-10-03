from django.urls import path, include

from . import views
urlpatterns = [
    path('authentication/', views.authentication, name="authentication")
]
