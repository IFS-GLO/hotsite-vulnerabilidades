from django.db import models


class Provider(models.Model):
    name = models.TextField(verbose_name='Nome')

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'


class Category(models.Model):
    name = models.TextField(verbose_name='Nome')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Software(models.Model):
    name = models.TextField(verbose_name='Nome')
    process_number = models.TextField(null=True, blank=True, verbose_name='Número do processo')
    version_stable = models.CharField(max_length=15, default='-', verbose_name='Versão estável')
    licenses_number = models.CharField(max_length=25, default='-', verbose_name='Número de licensas')
    license_validity = models.CharField(max_length=25, default='Perpétua', verbose_name='Vigência da licença')
    note = models.TextField(verbose_name='Obserçaões')

    provider = models.ForeignKey(Provider, verbose_name=Provider._meta.verbose_name)
    category = models.ForeignKey(Category, verbose_name=Category._meta.verbose_name)
