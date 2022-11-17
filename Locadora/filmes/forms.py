from django.forms import ModelForm
from .models import Filmes
class filmesForm(ModelForm):
    class Meta:
        model = Filmes
        fields = ['filme','genero','preco','quantidade']