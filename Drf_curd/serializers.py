from rest_framework import serializers
from .models import Drf_Curd


class Drf_curdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drf_Curd
        fields = ["id", "name", "description"]
