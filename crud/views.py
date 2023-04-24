from rest_framework import viewsets
from crud.models import revenues, expenses
from crud.serializer import RevenuesSerializer, ExpensesSerializer

class RevenuesViewSet(viewsets.ModelViewSet):
    """ Exibe todas as receitas cadastradas na base """
    queryset = revenues.objects.all()
    serializer_class = RevenuesSerializer

class ExpensesViewSet(viewsets.ModelViewSet):
    """ Exibe todas as despesas cadastradas na base """
    queryset = expenses.objects.all()
    serializer_class = ExpensesSerializer