from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import *


def providers(request):
    template_name = 'panel/list.html'

    instances = Provider.objects.all()

    context = {
        'head_title': 'Fornecedores',
        'instances': instances,
        'add_url': 'panel:catalog:add_provider',
        'edit_url': 'panel:catalog:provider',
        'del_url': 'panel:catalog:del_provider'
    }

    return render(request, template_name, context)


def add_provider(request):
    template_name = 'panel/add.html'

    form = ProviderForm(auto_id=False)

    if request.method == 'POST':
        form = ProviderForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            if Provider.objects.filter(name=name).exists():
                messages.error(request, 'Já existe.')

            else:
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


def del_provider(request, pk):
    if Provider.objects.filter(pk=pk).exists():
        Provider.objects.filter(pk=pk).delete()
        messages.success(request, 'Fornecedor removido com sucesso!')
    else:
        messages.error(request, 'Fornecedor não encontrado.')

    return redirect('panel:catalog:providers')


def categories(request):
    template_name = 'panel/list.html'

    instances = Category.objects.all()

    context = {
        'head_title': 'Categorias',
        'instances': instances,
        'add_url': 'panel:catalog:add_category',
        'edit_url': 'panel:catalog:category',
        'del_url': 'panel:catalog:del_category'
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


def del_category(request, pk):
    if Category.objects.filter(pk=pk).exists():
        Category.objects.filter(pk=pk).delete()
        messages.success(request, 'Categoria removida com sucesso!')
    else:
        messages.error(request, 'Categoria não encontrada.')

    return redirect('panel:catalog:categories')


def softwares(request):
    template_name = 'panel/list.html'

    instances = Software.objects.all()

    context = {
        'head_title': 'Softwares',
        'instances': instances,
        'add_url': 'panel:catalog:add_software',
        'edit_url': 'panel:catalog:software',
        'del_url': 'panel:catalog:del_software'
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


def del_software(request, pk):
    if Software.objects.filter(pk=pk).exists():
        Software.objects.filter(pk=pk).delete()
        messages.success(request, 'Software removido com sucesso!')
    else:
        messages.error(request, 'Software não encontrado.')

    return redirect('panel:catalog:softwares')


def vulnerabilities(request):
    template_name = 'panel/list.html'

    instances = Vulnerability.objects.all()

    context = {
        'head_title': 'Vulnerabilidades',
        'instances': instances,
        'add_url': 'panel:catalog:add_vulnerability',
        'edit_url': 'panel:catalog:vulnerability',
        'del_url': 'panel:catalog:del_vulnerability'
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

    if request.method == 'POST':
        list_products = request.POST.getlist('products')  # Get the products array and insert into a list

        request.POST._mutable = True  # For mutable the POST
        request.POST['products'] = list_products
        request.POST._mutable = False  # Return to no mutable

        form = VulnerabilityForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            messages.success(request, 'Atualizado com sucesso.')

    form = VulnerabilityForm(instance=instance)

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'form': form
    }

    return render(request, template_name, context)


def del_vulnerability(request, pk):
    if Vulnerability.objects.filter(pk=pk).exists():
        Vulnerability.objects.filter(pk=pk).delete()
        messages.success(request, 'Vulnerabilidade removida com sucesso!')
    else:
        messages.error(request, 'Vulnerabilidade não encontrada.')

    return redirect('panel:catalog:vulnerabilities')


def licenses(request):
    template_name = 'panel/list.html'

    instances = License.objects.all()

    context = {
        'head_title': 'Licenças',
        'instances': instances,
        'add_url': 'panel:catalog:add_license',
        'edit_url': 'panel:catalog:license',
        'del_url': 'panel:catalog:del_license'
    }

    return render(request, template_name, context)


def add_license(request):
    template_name = 'panel/add.html'

    form = LicenseForm(auto_id=False)

    if request.method == 'POST':
        form = LicenseForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Cadastrado com sucesso.')

    context = {
        'head_title': 'Nova Licença',
        'title': 'Licença',
        'form': form
    }

    return render(request, template_name, context)


def license(request, pk):
    template_name = 'panel/add.html'

    instance = License.objects.get(pk=pk)

    form = LicenseForm(auto_id=False, instance=instance)

    if request.method == 'POST':
        form = LicenseForm(request.POST or None, instance=instance)

        if form.is_valid():
            form.save()

            messages.success(request, 'Atualizado com sucesso.')

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'form': form
    }

    return render(request, template_name, context)


def del_license(request, pk):
    if License.objects.filter(pk=pk).exists():
        License.objects.filter(pk=pk).delete()
        messages.success(request, 'Licença removida com sucesso!')
    else:
        messages.error(request, 'Licença não encontrada.')

    return redirect('panel:catalog:licenses')
