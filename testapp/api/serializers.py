from rest_framework.serializers import ModelSerializer
from testapp.models import StudentModel


class StudentSerializer(ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
        