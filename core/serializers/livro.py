from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora, Autor, Livro
...
class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"