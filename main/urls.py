from django.urls import path

from .views import GroupListAPIView, GroupCreateAPIView, StudentListAPIView, StudentDetailAPIView

urlpatterns = [
    path('api/v1/students/', StudentListAPIView.as_view()),
    path('api/v1/students/<int:pk>/', StudentDetailAPIView.as_view()),
    path('api/v1/groups/', GroupListAPIView.as_view()),
    path('api/v1/group_create/', GroupCreateAPIView.as_view()),
    # path('api/v1/students/<int:pk>', StudentAPIView.as_view()),
]
