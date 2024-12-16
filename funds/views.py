from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fund
from .serializer import FundsSerializer
# Create your views here.

class FundDetail(APIView):
    def get(self, request, fund_id, format=None):
        try:
            fund = Fund.objects.get(fund_id=fund_id)
            serializer = FundsSerializer(fund)
            return Response(serializer.data)
        except Fund.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)