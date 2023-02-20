from rest_framework import serializers

from .models import Student, Group


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.surname = validated_data.get('surname', instance.surname)
        instance.name = validated_data.get('name', instance.name)
        instance.patronymic = validated_data.get('patronymic', instance.patronymic)
        instance.group_id = validated_data.get('group_id', instance.group_id)
        instance.save()
        return instance


class StudentNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['surname', 'name', 'patronymic']


class GroupSerializer(serializers.ModelSerializer):
    student = StudentNewSerializer()

    class Meta:
        model = Group
        fields = ['name', 'direction', 'student']

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        group = Group.objects.create(**validated_data)
        for student_dataa in student_data:
            Student.objects.create(group_id=group, **student_dataa)
        return group

    def update(self, instance, validated_data):
        student_data = validated_data.pop('student')
        student = instance.student

        instance.name = validated_data.get('name', instance.name)
        instance.direction = validated_data.get('direction', instance.direction)
        instance.save()

        student.surname = student_data.get('surname', student.surname)
        student.name = student_data.get('name', student.name)
        student.patronymic = student_data.get('patronymic', student.patronymic)
        student.save()

        return instance
