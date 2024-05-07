from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions as drf_permissions
from rest_framework import generics, authentication, views, status

from . import models
from . import permissions
from . import serializers

class StockListView(generics.ListAPIView):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer
    filterset_fields = ("name", "location")

class AuditDetailListView(generics.ListAPIView):
    queryset = models.AuditDetail.objects.all()
    serializer_class = serializers.AuditDetailSerializer

class ComputerListView(generics.ListAPIView):
    queryset = models.Computer.objects.all()
    serializer_class = serializers.ComputerSerializer

class StockRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.CustodianOrReadOnly ]

class ComputerRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Computer.objects.all()
    serializer_class = serializers.ComputerSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.CustodianOrReadOnly ]

class AuditDetailRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AuditDetail.objects.all()
    serializer_class = serializers.AuditDetailSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.AuditorOrReadOnly ]

class StockCreateView(generics.CreateAPIView):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.CustodianOrReadOnly ]

class ComputerCreateView(generics.CreateAPIView):
    queryset = models.Computer.objects.all()
    serializer_class = serializers.ComputerSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.CustodianOrReadOnly ]

class AuditDetailCreateView(generics.CreateAPIView):
    queryset = models.AuditDetail.objects.all()
    serializer_class = serializers.AuditDetailSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.AuditorOrReadOnly ]

class UsersView(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

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

class GetCurrentUserView(views.APIView):
    """
    Get username, email and role of the current logged in user
    """
    def get(self, request, format=None):
        user = serializers.UserSerializer(request.user).data

        return Response(user)

class CreateUserView(views.APIView):
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.IsHOD ]

    def post(self, request, format=None):
        if not (request.data.get("username") and request.data.get("password") and request.data.get("role")):
            return Response({"detail":"username, password and the role must be included in request"}, status=status.HTTP_400_BAD_REQUEST)
        
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        role = request.data.get("role")

        if email:
            user = models.User.objects.create_user(username=username, email=email, password=password, role=role)
        else:
            user = models.User.objects.create_user(username=username, password=password, role=role)

        serializeduser = serializers.UserSerializer(user).data

        return Response(serializeduser, status=status.HTTP_200_OK)

class GetLocationsView(views.APIView):
    def get(self, request, format=None):
        len = 0
        locations = dict()
        locations["results"] = []

        for i, j in models.LOCATIONS:
            len += 1
            locations["results"].append({"code": i, "name": j})

        locations["length"] = len

        return Response(locations, status=status.HTTP_200_OK)

class GetConditionsView(views.APIView):
    def get(self, request, format=None):
        len = 0
        conditions = dict()
        conditions["results"] = []

        for i, j in models.CONDITIONS:
            len += 1
            conditions["results"].append({"code": i, "name": j})

        conditions["length"] = len

        return Response(conditions, status=status.HTTP_200_OK)

class GetCategoriesView(views.APIView):
    def get(self, request, format=None):
        len = 0
        categories = dict()
        categories["results"] = []

        for i, j in models.CATEGORIES:
            len += 1
            categories["results"].append({"code": i, "name": j})

        categories["length"] = len

        return Response(categories, status=status.HTTP_200_OK)
