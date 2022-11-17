from django.db import models

class Generos(models.Model):
   genero = models.CharField('Genero', max_length=100)

   def __str__(self):
      return self.genero

   class Meta:
      verbose_name = 'Genero'
      verbose_name_plural = 'Generos'
      ordering = ['genero']

class Filmes(models.Model):
   filme = models.CharField('Nome', max_length=100)
   genero = models.ForeignKey(Generos, on_delete=models.PROTECT)
   preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
   quantidade = models.IntegerField('Quantidade', default=0)

   def __str__(self):
      return self.filme

   class Meta:
      verbose_name = 'Filme'
      verbose_name_plural = 'Filmes'
      ordering = ['filme']