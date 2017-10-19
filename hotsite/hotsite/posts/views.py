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
        'form_size': '8',
        'form': form,

    }

    return render(request, template_name, context)


def category(request, category_slug):
    template_name = 'hotsite/category.html'

    category = Category.objects.get(slug=category_slug)
    instances = Post.objects.filter(category=category).order_by('-created_at')

    context = {
        'head_title': category.name,
        'title': category.name,
        'instances': instances
    }

    return render(request, template_name, context)


def posts(request):
    pass


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
        'form_size': '8',
        'form': form,
    }

    return render(request, template_name, context)


def post(request, category_slug, post_slug):
    template_name = 'hotsite/post.html'

    instance = Post.objects.filter(slug=post_slug).filter(category__slug=category_slug)[0]

    context = {
        'head_title': instance.title,
        'title': instance.title,
        'instance': instance
    }

    return render(request, template_name, context)
