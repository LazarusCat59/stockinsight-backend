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

class AuditDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuditDetail
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'role')
