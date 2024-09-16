from rest_framework.viewsets import ModelViewSet

from core.serializers import CompraSerializer, CriarEditarCompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return CriarEditarCompraSerializer
        return CompraSerializer
