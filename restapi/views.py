from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class StockViewSet(viewsets.ModelViewSet):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer

class StockConditionViewSet(viewsets.ModelViewSet):
    queryset = models.StockCondition.objects.all()
    serializer_class = serializers.StockConditionSerializer

class AuditDetailsViewSet(viewsets.ModelViewSet):
    queryset = models.AuditDetails.objects.all()
    serializer_class = serializers.AuditDetailsSerializer
