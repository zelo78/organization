from django.urls import path
from django.views.generic import TemplateView

from organization.views import DivisionsDataView, EmployeeView

urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="index.html"), name="tree_of_employees"
    ),
    path("divisions/", DivisionsDataView.as_view(), name="divisions_by_head"),
    path("employee/", EmployeeView.as_view(), name="employee_card"),
]
