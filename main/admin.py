from django.contrib import admin

from .models import Student, Group


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'patronymic', 'group_id')
    list_display_links = ('id', 'surname')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'direction')
    list_display_links = ('id', 'name')


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
