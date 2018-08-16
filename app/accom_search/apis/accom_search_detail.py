from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accom_search.models import AccomSearchInfo
from accom_search.serializer import AccomDetailSerializer


class AccomSearchDetail(APIView):
    def get_object(self, pk):
        accomsearch_info = AccomSearchInfo.objects.get(pk=pk)
        accomsearch_info.accom_search_url()
        try:
            return AccomSearchInfo.objects.get(pk=pk)
        except AccomSearchInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        accomsearch_detail = self.get_object(pk).accomsearchinfodetail_set.first()
        serializer = AccomDetailSerializer(accomsearch_detail)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        accomsearch_detail = self.get_object(pk).accomsearchinfodetail_set.first()
        accomsearch_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
