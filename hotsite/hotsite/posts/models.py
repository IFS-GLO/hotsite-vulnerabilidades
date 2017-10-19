from django.db import models
from django.template.defaultfilters import slugify

from hotsite.settings import MEDIA_ROOT


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nome')
    slug = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name='Título')
    slug = models.CharField(max_length=30)
    content = models.TextField(verbose_name='Conteúdo')
    thumbnail = models.ImageField(upload_to=MEDIA_ROOT, null=True, blank=True, verbose_name='Imagem Destacada')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    category = models.ForeignKey(Category, verbose_name=Category._meta.verbose_name)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
