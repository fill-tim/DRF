from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Group
from .serializers import StudentListSerializer, StudentDetailSerializer, GroupListSerializer, \
    GroupCreateSerializer, StudentCreateSerializer


# class StudentListAPIView(APIView):
#     def get(self, request):
#         model = Student.objects.all()
#         serializer = StudentListSerializer(model, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StudentListSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer


class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentCreateSerializer


# class StudentDetailAPIView(APIView):
#     def get(self, request, pk):
#         student = Student.objects.get(id=pk)
#         serializer = StudentDetailSerializer(student)
#         return Response(serializer.data)
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'Метод PUT не работает!'})
#         try:
#             instance = Student.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Объект не найден!'})
#
#         serializer = StudentDetailSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'student': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'Метод DELETE не работает!'})
#         try:
#             instance = Student.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Объект не найден!'})
#
#         instance.delete()
#         return Response({'student': 'delete student with id = ' + str(pk)})


class StudentDetailsView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer


class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer


class StudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer


class GroupListAPIView(APIView):
    def get(self, request):
        group = Group.objects.all()
        serializer = GroupListSerializer(group, many=True)
        return Response(serializer.data)


class GroupCreateAPIView(APIView):
    def post(self, request):
        serializer = GroupCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'group': serializer.data})
