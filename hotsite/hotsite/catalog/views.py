from django.contrib import messages
from django.shortcuts import render

from .forms import *


def providers(request):
    template_name = 'panel/list.html'

    instances = Provider.objects.all()

    context = {
        'head_title': 'Fornecedores',
        'instances': instances,
        'add_url': 'panel:catalog:add_provider',
        'edit_url': 'panel:catalog:provider'
    }

    return render(request, template_name, context)


def add_provider(request):
    template_name = 'panel/add.html'

    form = ProviderForm(auto_id=False)

    if request.method == 'POST':
        form = ProviderForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Cadastrado com sucesso.')

    context = {
        'head_title': 'Novo Fornecedor',
        'title': 'Fornecedor',
        'form': form
    }

    return render(request, template_name, context)


def provider(request, pk):
    template_name = 'panel/add.html'

    instance = Provider.objects.get(pk=pk)

    form = ProviderForm(auto_id=False, instance=instance)

    if request.method == 'POST':
        form = ProviderForm(request.POST or None, instance=instance)

        if form.is_valid():
            form.save()

            messages.success(request, 'Atualizado com sucesso.')

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'form': form
    }

    return render(request, template_name, context)


def categories(request):
    template_name = 'panel/list.html'

    instances = Category.objects.all()

    context = {
        'head_title': 'Categorias',
        'instances': instances,
        'add_url': 'panel:catalog:add_category',
        'edit_url': 'panel:catalog:category'
    }

    return render(request, template_name, context)


def add_category(request):
    template_name = 'panel/add.html'

    form = CategoryForm(auto_id=False)

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Cadastrado com sucesso.')

    context = {
        'head_title': 'Nova Categoria',
        'title': 'Categoria',
        'form': form
    }

    return render(request, template_name, context)


def category(request, pk):
    template_name = 'panel/add.html'

    instance = Category.objects.get(pk=pk)

    form = CategoryForm(auto_id=False, instance=instance)

    if request.method == 'POST':
        form = CategoryForm(request.POST or None, instance=instance)

        if form.is_valid():
            form.save()

            messages.success(request, 'Atualizado com sucesso.')

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'form': form
    }

    return render(request, template_name, context)


def softwares(request):
    template_name = 'panel/list.html'

    instances = Software.objects.all()

    context = {
        'head_title': 'Softwares',
        'instances': instances,
        'add_url': 'panel:catalog:add_software',
        'edit_url': 'panel:catalog:software'
    }

    return render(request, template_name, context)


def add_software(request):
    template_name = 'panel/add.html'

    form = SoftwareForm(auto_id=False)

    if request.method == 'POST':
        form = SoftwareForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Cadastrado com sucesso.')

    context = {
        'head_title': 'Novo Software',
        'title': 'Software',
        'form': form
    }

    return render(request, template_name, context)


def software(request, pk):
    template_name = 'panel/add.html'

    instance = Software.objects.get(pk=pk)

    form = SoftwareForm(auto_id=False, instance=instance)

    if request.method == 'POST':
        form = SoftwareForm(request.POST or None, instance=instance)

        if form.is_valid():
            form.save()

            messages.success(request, 'Atualizado com sucesso.')

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'form': form
    }

    return render(request, template_name, context)


def vulnerabilities(request):
    template_name = 'panel/list.html'

    instances = Vulnerability.objects.all()

    context = {
        'head_title': 'Vulnerabilidades',
        'instances': instances,
        'add_url': 'panel:catalog:add_vulnerability',
        'edit_url': 'panel:catalog:vulnerability'
    }

    return render(request, template_name, context)


def add_vulnerability(request):
    template_name = 'panel/add.html'

    form = VulnerabilityForm(auto_id=False)

    if request.method == 'POST':
        list_products = request.POST.getlist('products')  # Get the products array and insert into a list

        request.POST._mutable = True  # For mutable the POST
        request.POST['products'] = list_products
        request.POST._mutable = False  # Return to no mutable

        form = VulnerabilityForm(request.POST)

        if form.is_valid():
            form.save()
            form = VulnerabilityForm(auto_id=False)

            messages.success(request, 'Cadastrado com sucesso.')

        else:
            pass

    context = {
        'head_title': 'Nova vulnerabilidade',
        'title': 'Vulnerabilidade',
        'form': form
    }

    return render(request, template_name, context)


def vulnerability(request, pk):
    template_name = 'panel/add.html'

    instance = Vulnerability.objects.get(pk=pk)

    form = VulnerabilityForm(instance=instance)

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'form': form
    }

    return render(request, template_name, context)
