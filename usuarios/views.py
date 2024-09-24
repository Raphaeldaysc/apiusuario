from rest_framework import viewsets
from .models import Usuario  # Ajuste esta importação conforme o nome da sua classe de modelo
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()  # Queryset para recuperar todas as instâncias de usuário
    serializer_class = UsuarioSerializer  # Especifica a classe serializer para serialização/deserialização

    def perform_create(self, serializer):
        # Comportamento personalizado para criar um usuário (se necessário)
        serializer.save()  # Salva a instância de usuário
