from django.urls import path
from .views import *

urlpatterns = [
    path('vidu/', ViDuView.as_view(), name='vidu'),
    path('get_all_students/', StudentView.as_view(), name='get_all_students'),
]
