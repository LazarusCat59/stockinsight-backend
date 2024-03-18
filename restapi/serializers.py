from rest_framework import serializers
from . import models 

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stock
        fields = '__all__'

class StockConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StockCondition
        fields = '__all__'

class AuditDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuditDetails
        fields = '__all__'
