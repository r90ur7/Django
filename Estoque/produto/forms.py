from django.forms import ModelForm
from .models import Produtos
class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ["produto","cor"]
