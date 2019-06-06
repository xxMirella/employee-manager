from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from manager.core.models import Employee
from manager.core.models.serializer.employee_serializer import EmployeeSerializer


@api_view(['GET'])
@permission_classes((AllowAny,))
def list_employee(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

