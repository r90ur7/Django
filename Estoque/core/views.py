from django.shortcuts import render
def index(request):
    template_name = 'index.html'
    context ={
        'mensagem': 'Bem vindo a apliccação estoque web'
    }
    return render(request,template_name,context)
# Create your views here.
