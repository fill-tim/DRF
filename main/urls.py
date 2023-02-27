from django.urls import path

from .views import GroupListAPIView, GroupCreateAPIView, StudentListView, StudentCreateView, StudentDetailsView, \
    StudentUpdateView, StudentView

urlpatterns = [
    # path('api/v1/students/', StudentListAPIView.as_view()),
    path('api/v1/students/', StudentListView.as_view()),
    # path('api/v1/students/<int:pk>/', StudentDetailAPIView.as_view()),
    path('api/v1/students/<int:pk>/', StudentView.as_view()),
    # path('api/v1/students/<int:pk>/', StudentDetailsView.as_view()),
    # path('api/v1/students_update/<int:pk>/', StudentUpdateView.as_view()),
    path('api/v1/groups/', GroupListAPIView.as_view()),
    path('api/v1/group_create/', GroupCreateAPIView.as_view()),
    path('api/v1/student_create/', StudentCreateView.as_view()),
    # path('api/v1/students/<int:pk>', StudentAPIView.as_view()),
]
