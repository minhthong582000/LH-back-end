from menu.models import Menu

from rest_framework import viewsets, permissions
from .serializers import MenuSerializer

# Menu Viewset
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MenuSerializer