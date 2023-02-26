from rest_framework import serializers

from .models import Student, Group


class StudentListSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['group']


class GroupListSerializer(serializers.ModelSerializer):
    student = StudentDetailSerializer(many=True)

    class Meta:
        model = Group
        fields = ['name', 'direction', 'student']


class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
