from django.urls import path
from django.views.generic import TemplateView

from organization.views import TreeDataView

# from files.views import (
#     FileGetDeleteView,
#     FileListCreateView,
#     FileUploadView,
#     FileListView,
#     FileDownloadView,
#     StatisticFileView,
#     HealthView,
# )

urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="index.html"), name="tree_of_employees"
    ),
    path("tree/", TreeDataView.as_view(), name="tree_data"),
    # path("download", FileUploadView.as_view(), name="file_upload"),
    # path("file", FileListView.as_view(), name="file_list_view"),
    # path("file/<int:file_id>", FileDownloadView.as_view(), name="file_download_view"),
    # path(
    #     "data/",
    #     FileListCreateView.as_view(),
    #     name="file_list_create",
    # ),
    # path(
    #     "data/<int:file_id>/",
    #     FileGetDeleteView.as_view(),
    #     name="file_get_delete",
    # ),
    # path("statistic/", StatisticFileView.as_view(), name="uploaded_file_statistic"),
    # path("health/", HealthView.as_view(), name="health_view"),
]
