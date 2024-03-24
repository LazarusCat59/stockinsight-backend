from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class StockViewSet(viewsets.ModelViewSet):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer

class StockTypeViewSet(viewsets.ModelViewSet):
    queryset = models.StockType.objects.all()
    serializer_class = serializers.StockTypeSerializer

class AuditDetailsViewSet(viewsets.ModelViewSet):
    queryset = models.AuditDetails.objects.all()
    serializer_class = serializers.AuditDetailsSerializer
