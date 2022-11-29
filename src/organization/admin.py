from django.contrib import admin

from organization.models import Division, Employee


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ["name", "head"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "patronymic", "division", "position"]
    search_fields = ["last_name", "first_name", "patronymic"]
    search_help_text = "Поиск сотрудника по ФИО или его части"
