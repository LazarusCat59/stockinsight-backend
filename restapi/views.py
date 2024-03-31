from django.shortcuts import render
from rest_framework import generics, authentication, views, status
from rest_framework import permissions as drf_permissions
from rest_framework.response import Response
from . import permissions
from . import models
from . import serializers

class StockListView(generics.ListAPIView):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer

class StockTypeListView(generics.ListAPIView):
    queryset = models.StockType.objects.all()
    serializer_class = serializers.StockTypeSerializer

class AuditDetailsListView(generics.ListAPIView):
    queryset = models.AuditDetails.objects.all()
    serializer_class = serializers.AuditDetailsSerializer

class StockRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.CustodianOrReadOnly ]

class StockTypeRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StockType.objects.all()
    serializer_class = serializers.StockTypeSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.CustodianOrReadOnly ]

class AuditDetailsRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AuditDetails.objects.all()
    serializer_class = serializers.AuditDetailsSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.AuditorOrReadOnly ]

class StockCreateView(generics.CreateAPIView):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.CustodianOrReadOnly ]

class StockTypeCreateView(generics.CreateAPIView):
    queryset = models.StockType.objects.all()
    serializer_class = serializers.StockTypeSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.CustodianOrReadOnly ]

class AuditDetailsCreateView(generics.CreateAPIView):
    queryset = models.AuditDetails.objects.all()
    serializer_class = serializers.AuditDetailsSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.AuditorOrReadOnly ]

class StockSearchView(views.APIView):
    """
    View used for searching stock with name parameter
    """
    def get(self, request, format=None):
        if not request.GET.get("name"):
            return Response({"detail":"name must be included in request"}, status=status.HTTP_400_BAD_REQUEST)

        stocks = [serializers.StockSerializer(s).data for s in models.Stock.objects.all() if s.name.startswith(request.GET.get("name"))]

        if(stocks):
            return Response(stocks)
        else:
            return Response({"detail":"No stocks starting with given name found"}, status=status.HTTP_404_NOT_FOUND)

class StockTypeSearchView(views.APIView):
    """
    View used for searching stock with name parameter
    """
    def get(self, request, format=None):
        if not request.GET.get("name"):
            return Response({"detail":"name must be included in request"}, status=status.HTTP_400_BAD_REQUEST)

        stocktypes = [serializers.StockTypeSerializer(s).data for s in models.StockType.objects.all() if s.name.startswith(request.GET.get("name"))]

        if(stocktypes):
            return Response(stocktypes)
        else:
            return Response({"detail":"No stocks starting with given name found"}, status=status.HTTP_404_NOT_FOUND)
