from django.contrib import admin

from organization.models import Division, Employee


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ["name", "head"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "patronymic", "division", "position"]
