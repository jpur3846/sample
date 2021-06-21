from django.urls import path, include

from .views import DataEndpoint

urlpatterns = [
    path('data/', DataEndpoint.as_view(), name='DataEndpoint'),
]