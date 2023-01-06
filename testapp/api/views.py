from rest_framework  import viewsets
from testapp.models import StudentModel
from testapp.api.serializers import StudentSerializer

class StudentCRUD(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    

