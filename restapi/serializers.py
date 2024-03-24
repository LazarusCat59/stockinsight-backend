from rest_framework import serializers
from . import models 

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stock
        fields = '__all__'

class StockTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StockType
        fields = '__all__'

class AuditDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuditDetails
        fields = '__all__'
