from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField
from core.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade", "total")
        depth = 1



class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")



class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
        usuario = CharField(source="usuario.email", read_only=True) # inclua essa linha
        status = CharField(source="get_status_display", read_only=True) # inclua essa linha
        itens = ItensCompraSerializer(many=True, read_only=True)


class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True) # Aqui mudou

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return compra