from django.shortcuts import render
from rest_framework.generics import (ListAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView)
from rest_framework.views import APIView, Request, Response, status
from .serializers import CNABdocSerializer,CNABentriesSerializer
from .models import CNABdoc, CNABfile
from utils.mixins import SerializerByMethodMixin
import ipdb

# Create your views here.

class ListCNABView(SerializerByMethodMixin,ListCreateAPIView):
    serializer_class= CNABdocSerializer
    queryset = CNABdoc.objects.all()

    serializer_map = {
        "GET": CNABentriesSerializer,
        "POST": CNABdocSerializer,
    }

class ListOneCNABView(RetrieveUpdateDestroyAPIView):
    serializer_class= CNABdocSerializer
    queryset = CNABfile.objects.all()
    lookup_url_kwarg = "pk"

class ListAllStoreCNABView(ListAPIView):

    serializer_class= CNABentriesSerializer
    queryset= CNABdoc.objects.all()
    lookup_url_kwarg ="cpf"

    def get_queryset(self):
        cpfget = self.kwargs.get(self.lookup_url_kwarg)
        transactions = CNABdoc.objects.filter(cpf= cpfget)

        return transactions

class ListBalanceStoreView(APIView):

    def get(self, request: Request, cpf: int) -> Response:

        entries= CNABdoc.objects.filter(cpf = cpf)

        serializer = CNABentriesSerializer(entries, many=True)

        balance = 0

        for item in serializer.data:
            if item['type'] == 2 or item['type'] == 2 or item['type'] == 9:
                balance = balance - item['value']
            balance = balance + item['value']

        return Response({"account_balance": balance ,"transactions": serializer.data})