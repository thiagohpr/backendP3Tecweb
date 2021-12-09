from rest_framework import serializers
from .models import Lista


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = ['id', 'title', 'score', 'state', 'url']