from .models import *
from rest_framework import serializers


class ProdutosSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Produtos
        fields = '__all__'
    