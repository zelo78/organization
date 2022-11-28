from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from organization.models import Division


class TreeDataView(APIView):
    def get(self, request):
        parent_id = request.query_params.get("parentId")
        if parent_id is None:
            parent = None
        else:
            try:
                parent = Division.objects.get(id=parent_id)
            except Division.DoesNotExist:
                return Response(data=[])

        data = []
        for division in Division.objects.filter(head=parent).order_by("name"):
            data.append(
                {
                    "id": division.id,
                    "@checked": False,
                    "text": f"<b>{division.name}<b>",
                    "has_children": division.subordinates.values_list("id", flat=True),
                    "population": 10000,
                }
            )

        # data1 = {
        #     "id" : 2022,
        #     "text": "l.Name",
        #     #@checked= l.Checked,
        #     "population": 123456,
        #     # flagUrl = l.FlagUrl,
        #     "hasChildren": False # = locations.Any(l2= > l2.ParentID == l.ID)
        # }
        # data = [data1]

        return Response(data=data, status=status.HTTP_200_OK)
