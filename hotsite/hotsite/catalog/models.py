from django.db import models


class Provider(models.Model):
    name = models.TextField(verbose_name='Nome')

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.TextField(verbose_name='Nome')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Software(models.Model):
    name = models.TextField(verbose_name='Nome')
    process_number = models.TextField(null=True, blank=True, verbose_name='Número do processo')
    version_stable = models.CharField(max_length=15, default='-', verbose_name='Versão estável')
    licenses_number = models.CharField(max_length=25, default='-', verbose_name='Número de licensas')
    license_validity = models.CharField(max_length=25, default='Perpétua', verbose_name='Vigência da licença')
    note = models.TextField(verbose_name='Obserçaões')

    provider = models.ForeignKey(Provider, verbose_name=Provider._meta.verbose_name)
    category = models.ForeignKey(Category, verbose_name=Category._meta.verbose_name)

    def __str__(self):
        return self.name


class Vulnerability(models.Model):
    SEVERITY_CHOICES = (
        ('Cuidado', 'Cuidado'),
        ('Alto', 'Alto'),
        ('Crítico', 'Crítico')
    )

    name = models.TextField(verbose_name='Nome')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    solution = models.TextField(verbose_name='Solução')
    severity = models.CharField(max_length=7, choices=SEVERITY_CHOICES, verbose_name='Gravidade')

    detected_at = models.DateField(verbose_name='Detectado em')
    created_at = models.DateField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateField(auto_now=True, verbose_name='Atualizado em')

    products = models.ManyToManyField(Software, verbose_name=Software._meta.verbose_name_plural)

    class Meta:
        verbose_name = 'Vulnerabilidade'

    def __str__(self):
        return self.name
