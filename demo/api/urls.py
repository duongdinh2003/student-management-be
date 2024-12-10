from django.urls import path, include

urlpatterns = [
    path('student/', include('api.student.urls')),
]
