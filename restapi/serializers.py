from rest_framework import serializers
from . import models 

class StockSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.Stock
        fields = '__all__'
        extra_kwargs = {
                'url': { 'view_name' : 'stock-detail' },
                'type' : { 'view_name' : 'stocktype-detail' },
                'audit_details' : { 'view_name' : 'audit-detail' },
        }

class StockTypeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.StockType
        fields = '__all__'
        extra_kwargs = {
                'url': { 'view_name' : 'stocktype-detail' },
        }

class AuditDetailSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
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

class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.Computer
        fields = '__all__'
        extra_kwargs = {
                'url' : { 'view_name' : 'computer-detail' },
                'keyboard' : { 'view_name' : 'stock-detail' },
                'mouse' : { 'view_name' : 'stock-detail' },
                'monitor' : { 'view_name' : 'stock-detail' },
                'cpu' : { 'view_name' : 'stock-detail' },
        }
