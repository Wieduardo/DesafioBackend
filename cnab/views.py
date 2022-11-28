from django.shortcuts import render
from rest_framework.generics import (ListAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView)
from .serializers import CNABdocSerializer,CNABentriesSerializer
from .models import CNABdoc, CNABfile
from utils.mixins import SerializerByMethodMixin

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
