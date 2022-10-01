from rest_framework import serializers
from .models import Paint


class PaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paint
        fields = "__all__"
