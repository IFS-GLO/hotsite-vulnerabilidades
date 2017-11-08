from django.contrib import messages
from django.shortcuts import render

from hotsite.posts.forms import *


def add_category(request):
    template_name = 'add.html'
    title = 'Nova categoria'

    form = CategoryForm(auto_id=False)

    if request.method == 'POST':
        form = CategoryForm(request.POST or None)

        if form.is_valid():
            form.save()
            title = form.instance.name

            messages.success(request, 'Cadastrado com sucesso!')

    context = {
        'head_title': title,
        'title': title,
        'form': form,
        'form_size': '8',

    }

    return render(request, template_name, context)


def category(request, category_slug):
    template_name = 'add.html'

    instance = Category.objects.get(slug=category_slug)
    form = CategoryForm(instance=instance)

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'form': form,
        'form_size': '8',
    }

    return render(request, template_name, context)


def view_category(request, category_slug):
    template_name = 'hotsite/category.html'

    instance = Category.objects.get(slug=category_slug)
    instances = Post.objects.filter(category=instance)

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'instances': instances,
    }

    return render(request, template_name, context)


def categories(request):
    template_name = 'list.html'

    instances = Category.objects.all()

    context = {
        'head_title': 'Categorias',
        'title': 'Categorias',
        'instances': instances,
        'add_url': 'panel:posts:add_category',
        'edit_url': 'panel:posts:category'
    }

    return render(request, template_name, context)


def posts(request):
    template_name = 'list_post.html'

    instances = Post.objects.all()

    context = {
        'head_title': 'Post',
        'title': 'Post',
        'instances': instances
    }

    return render(request, template_name, context)


def add_post(request):
    template_name = 'add.html'
    title = 'Nova notícia'

    form = PostForm(auto_id=False)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            title = form.instance.title

            messages.success(request, 'Cadastrado com sucesso!')

        else:
            messages.error(request, 'Falha ao cadastrar.')

    context = {
        'head_title': title,
        'title': title,
        'form': form,
        'form_size': '8',
    }

    return render(request, template_name, context)


def view_post(request, category_slug, post_slug):
    template_name = 'hotsite/post.html'

    instance = Post.objects.filter(slug=post_slug).filter(category__slug=category_slug)[0]

    context = {
        'head_title': instance.title,
        'title': instance.title,
        'instance': instance
    }

    return render(request, template_name, context)


def post(request, post_slug):
    template_name = 'add.html'

    instance = Post.objects.get(slug=post_slug)
    form = PostForm(instance=instance)

    context = {
        'head_title': instance.title,
        'title': instance.title,
        'instance': instance,
        'form': form,
        'form_size': 8
    }

    return render(request, template_name, context)

