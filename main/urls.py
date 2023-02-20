from django.urls import path

from .views import StudentAPIList

urlpatterns = [
    # path('api/v1/students/', StudentAPIView.as_view()),
    path('api/v1/students/', StudentAPIList.as_view()),
    path('api/v1/students/<int:pk>', StudentAPIList.as_view()),
    # path('api/v1/students/<int:pk>', StudentAPIView.as_view()),
]
