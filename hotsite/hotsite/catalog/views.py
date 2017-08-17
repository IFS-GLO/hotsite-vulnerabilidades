from django.contrib import messages
from django.shortcuts import render

from .forms import *


def providers(request):
    template_name = 'panel/list.html'

    instances = Provider.objects.all()

    context = {
        'instances': instances
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
