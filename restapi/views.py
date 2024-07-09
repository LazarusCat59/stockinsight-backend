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

class AssignmentCreateView(generics.CreateAPIView):
    queryset = models.Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.IsHOD ]

class AssignmentListView(generics.ListAPIView):
    queryset = models.Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer

class AssignmentRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer

class StockSearchView(views.APIView):
    """
    View used for searching stock with name parameter
    """
    def get(self, request, format=None):
        if not request.data.get("name"):
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
        serializer_context = {
                'request' : request
        }

        user = serializers.UserSerializer(request.user, context=serializer_context).data

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

        serializer_context = {
                'request' : request
        }

        serialized_user = serializers.UserSerializer(user, context=serializer_context).data

        return Response(serialized_user, status=status.HTTP_201_CREATED)

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

class GetAuditedStocksView(views.APIView):
    def get(self, request, format=None):
        auditedstocks = models.Stock.objects.exclude(audit_details=None)
        count = len(auditedstocks)

        serializer_context = {
                'request' : request
        }

        serializedstocks = [serializers.StockSerializer(x, context=serializer_context).data for x in auditedstocks]

        return Response({"count" : count, "results" : serializedstocks, "previous" : None, "next" : None}, status = status.HTTP_200_OK)

class GetUnassignedAuditorView(views.APIView):
    def get(self, request, format=None):
        auditors = models.User.objects.filter(role="ADT")
        assigned_auditors = [x.auditor for x in models.Assignment.objects.all()]

        serializer_context = {
                'request' : request
        }

        unassigned_auditors = [serializers.UserSerializer(x, context=serializer_context).data for x in auditors if x not in assigned_auditors]
        count = len(unassigned_auditors)

        return Response({ "count" : count, "results" : unassigned_auditors, "previous" : None, "next" : None}, status = status.HTTP_200_OK)

class GetAssignmentView(views.APIView):
    def get(self, request, format=None):
        try:
            assignment = models.Assignment.objects.get(auditor=request.user)
        except models.Assignment.DoesNotExist:
            assignment = None

        serializer_context = {
                'request' : request
        }
        
        if assignment:
            serialized_assignment = serializers.AssignmentSerializer(assignment, context=serializer_context).data
            return Response(serialized_assignment, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "No assignments available"}, status=status.HTTP_204_NO_CONTENT)

class AttachAudit(views.APIView):
    permission_classes = [ drf_permissions.IsAuthenticated, permissions.IsAuditor ]
    def post(self, request, format=None):
        stock_id = request.data.get("stock_id")
        audit_id = request.data.get("audit_id")

        if not (stock_id and audit_id):
            return Response({"detail":"stock_id and audit_id must be included in request"}, status=status.HTTP_400_BAD_REQUEST)

        serializer_context = {
                'request' : request
        }

        try:
            stock = models.Stock.objects.get(id=stock_id)
        except models.Stock.DoesNotExist:
            return Response({"detail": "No stock found with given ID"}, status=status.HTTP_404_NOT_FOUND)

        try:
            audit = models.AuditDetail.objects.get(id=audit_id)
        except models.AuditDetail.DoesNotExist:
            return Response({"detail": "No audit found with given ID"}, status=status.HTTP_404_NOT_FOUND)
        
        stock.audit_details = audit
        stock.save()

        serialized_stock = serializers.StockSerializer(stock, context=serializer_context).data
        return Response(serialized_stock, status=status.HTTP_201_CREATED)
