from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .models.serializer.employee_serializer import EmployeeSerializer


class EmployeeView(generics.ListCreateAPIView):
    permission_classes = IsAuthenticated
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
