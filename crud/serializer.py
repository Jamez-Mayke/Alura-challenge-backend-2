from rest_framework import serializers
from crud.models import revenues, expenses

class RevenuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = revenues
        fields = ['id', 'descricao', 'valor', 'data']

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = expenses
        fields = ['id', 'descricao', 'valor', 'data']