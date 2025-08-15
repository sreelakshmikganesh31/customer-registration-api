
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):#ModelViewSet in DRF it automatically gives you all CRUD operations in one class
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
