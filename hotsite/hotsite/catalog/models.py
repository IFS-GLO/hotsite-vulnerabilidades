from django.db import models
from django.contrib.auth.models import User


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


class License(models.Model):
    name = models.CharField(max_length=25, verbose_name='Nome')

    class Meta:
        verbose_name = 'Licença'
        verbose_name_plural = 'Licenças'

    def __str__(self):
        return self.name


class TypeUse(models.Model):
    name = models.CharField(max_length=25, verbose_name='Nome')

    class Meta:
        verbose_name = 'Tipo de uso'
        verbose_name_plural = 'Tipo de uso'

    def __str__(self):
        return self.name


class Software(models.Model):
    name = models.TextField(verbose_name='Nome')
    process_number = models.TextField(null=True, blank=True, verbose_name='Número do processo')
    version_stable = models.CharField(max_length=15, default='-', verbose_name='Versão estável')
    licenses_number = models.CharField(max_length=25, default='-', verbose_name='Número de licenças')
    note = models.TextField(verbose_name='Observações')

    license = models.ForeignKey(License, default=1, verbose_name=License._meta.verbose_name)
    type = models.ForeignKey(TypeUse, null=True, blank=True, verbose_name=TypeUse._meta.verbose_name)
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
    has_kaspersky = models.BooleanField(default=False, verbose_name='Está no catálogo da Kaspersky?')

    detected_at = models.DateField(verbose_name='Detectado em')
    created_at = models.DateField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateField(auto_now=True, verbose_name='Atualizado em')

    products = models.ManyToManyField(Software, verbose_name=Software._meta.verbose_name_plural)
    fixed = models.ManyToManyField(User, through='WhoFixed', verbose_name='Usuários')

    class Meta:
        verbose_name = 'Vulnerabilidade'

    def __str__(self):
        return self.name


class WhoFixed(models.Model):
    fixed_at = models.DateTimeField(auto_now_add=True, verbose_name='Corrigido em')

    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name)
    vulnerability = models.ForeignKey(Vulnerability, verbose_name=Vulnerability._meta.verbose_name)

    class Meta:
        verbose_name = 'Quem corrigiu'

    def __str__(self):
        return self.user
