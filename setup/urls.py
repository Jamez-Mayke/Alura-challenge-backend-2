from django.contrib import admin
from django.urls import path, include
from crud.views import RevenuesViewSet, ExpensesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('receitas', RevenuesViewSet, basename='revenues')
router.register('despesas', ExpensesViewSet, basename='expenses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
