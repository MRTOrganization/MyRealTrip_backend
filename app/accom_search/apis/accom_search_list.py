from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accom_search.models import AccomSearchInfo
from accom_search.serializer import AccomSerializer, AccomDetailSerializer


class AccomSearchList(APIView):
    def get(self, request, format=None):
        accom_searchs = AccomSearchInfo.objects.all()
        serializer = AccomSerializer(accom_searchs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_accom_search = AccomSearchInfo.objects.latest('pk')
            new_accom_search.accom_search_url()
            detail_serializer = AccomDetailSerializer(new_accom_search.accomsearchinfodetail_set.first())
            return Response(detail_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
