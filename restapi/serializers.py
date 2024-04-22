from rest_framework import serializers
from . import models 

class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Stock
        fields = '__all__'
        extra_kwargs = {
                'url': { 'view_name' : 'stock-detail' },
                'type' : { 'view_name' : 'stocktype-detail' },
        }

class StockTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.StockType
        fields = '__all__'
        extra_kwargs = {
                'url': { 'view_name' : 'stocktype-detail' },
        }

class AuditDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AuditDetail
        fields = '__all__'
        extra_kwargs = {
                'url': { 'view_name' : 'audit-detail' },
        }

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'role')
