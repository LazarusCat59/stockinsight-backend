from rest_framework import serializers
from . import models 

class StockSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.Stock
        fields = '__all__'
        extra_kwargs = {
                'url': { 'view_name' : 'stock-detail' },
                'audit_details' : { 'view_name' : 'audit-detail' },
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
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.User
        fields = ('id', 'url', 'username', 'email', 'role')
        extra_kwargs = {
                'url' : { 'view_name' : 'user-detail' },
        }

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

class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.Assignment
        fields = '__all__'
