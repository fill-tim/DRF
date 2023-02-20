from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Group
from .serializers import StudentSerializer, StudentNewSerializer, GroupSerializer


# Create your views here.
# class StudentAPIView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentAPIView(APIView):
#     def get(self, request):
#         model = Student.objects.all().values()
#         return Response({'students': list(model)})
#
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'student': serializer.data})
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
#         serializer = StudentSerializer(data=request.data, instance=instance)
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
#
#
class StudentAPIList(generics.UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
