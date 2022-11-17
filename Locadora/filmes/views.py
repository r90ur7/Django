from django.shortcuts import render, redirect, get_object_or_404
from django.urls import is_valid_path
from .models import Filmes
from .forms import filmesForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator

def index(request):
    template_name = 'index.html'
    context = {
        'página':'UGB-Ferp Locadora'
    }
    return render(request, template_name,context)

def list_filmes(request):
    filmes =Filmes.objects.all()
    template_name = 'list_filmes.html'
    context = {
        'filmes': filmes,
        'página': 'Lista de Filmes',
    }
    return render(request, template_name, context)
# @login_required
def New_filmes(request):
    form = filmesForm()

    if(request.method == 'POST'):

        form = filmesForm(request.POST)

        if(form.is_valid()):
            post_title = form.cleaned_data['filme']
            post_slug = form.cleaned_data['genero']
            post_body = form.cleaned_data['preco']
            post_author = form.cleaned_data['quantidade']
            new_post = Filmes(filme=post_title, genero=post_slug, preco=post_body, quantidade=post_author)
            new_post.save()

            return redirect('filme:list_filmes')

    elif(request.method == 'GET'):
        return render(request,'filme_new.html', {'form': form})
    filmes =Filmes.objects.all()
    template_name = 'filme_new.html'
    context = {
        'filmes': filmes,
        'página': 'Novo Filme',
    }
    return render(request, template_name,context)
def  Del_filmes(request,pk):
    filme =Filmes.objects.get(id=pk)
    filme.delete()
    return redirect("filme:list_filmes")

def Edit_filmes(request,pk):
    filme =Filmes.objects.get(id=pk)
    template_name = 'filmes_edit.html'
    if request.method == "POST":
        form = filmesForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect("filme:list_filmes")
    else:
        context = {
            'form': filmesForm(instance=filme),
            "pk": pk,
            'página': 'Editar Filmes',
        }
    return render(request, template_name, context)

