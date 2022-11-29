from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from organization.models import Division, Employee


class DivisionsDataView(APIView):
    def get(self, request):
        head_id = request.query_params.get("head", 0)
        head = Division.objects.filter(id=head_id).first()

        data = []

        for division in Division.objects.filter(head=head).order_by("name"):
            item = {
                "label": division.name,
                "isFolder": True,
                "path": division.id,
                "isDrive": (division.head is None),
                "hasSubfolder": division.subordinates.exists(),
            }
            data.append(item)
        if head is not None:
            for employee in head.employees.order_by(
                "last_name", "first_name", "patronymic"
            ):
                item = {
                    "label": employee.full_name,
                    "isFolder": False,
                    "path": employee.id,
                    "subitems": [
                        employee.position,
                        employee.date_of_employment.strftime("%d.%m.%Y"),
                        employee.wage,
                    ],
                }
                data.append(item)

        return Response(data=data, status=status.HTTP_200_OK)


class EmployeeView(TemplateView):
    template_name = "organization/employee.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_id = self.request.GET.get("path")
        employee = get_object_or_404(Employee, id=employee_id)
        context["employee"] = employee
        context["division"] = employee.division
        return context
