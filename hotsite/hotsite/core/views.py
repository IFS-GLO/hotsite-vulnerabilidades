from datetime import date, timedelta

from django.db.models import Count
from django.shortcuts import render

from hotsite.catalog.models import Vulnerability, Provider, Software, WhoFixed
from hotsite.posts.models import Post


def index(request):
    template_name = 'hotsite/index.html'
    title = 'Vulnerabilidades'

    if request.method == 'POST':
        if request.user.id:
            vulnerability_id = request.POST['vulnerability']

            instance = Vulnerability.objects.get(pk=int(vulnerability_id))
            WhoFixed(vulnerability=instance, user=request.user).save()

    instances = Vulnerability.objects.all()

    posts = Post.objects.all().order_by('-updated_at')[:8]

    # To check if user has fixed the vulnerability
    if request.user.id:
        for v in instances:
            if WhoFixed.objects.filter(user=request.user).filter(vulnerability=v).exists():
                fixed = True

            else:
                fixed = False

            v.whofixed = fixed

    context = {
        'title': title,
        'instances': instances,
        'posts': posts,
    }

    return render(request, template_name, context)


def catalog(request):
    template_name = 'hotsite/catalog.html'

    instances = Software.objects.all()

    context = {
        'head_title': 'Catálogo de Software',
        'title': 'Catálogo de Software',
        'instances': instances
    }

    return render(request, template_name, context)


def providers(request):
    template_name = 'hotsite/providers.html'
    title = 'Fornecedores'

    instances = Provider.objects.all()
    arr_providers = []

    for instance in instances:
        # TODO: Get the product with the most vulnerabilities registered and the last update

        provider = {
            'provider': instance,
            'products': Software.objects.filter(provider=instance),
        }

        arr_providers.append(provider)

    instances = arr_providers

    context = {
        'title': title,
        'instances': instances
    }

    return render(request, template_name, context)


def provider(request, pk):
    template_name = 'hotsite/provider.html'

    instance = Provider.objects.get(pk=pk)
    instances = Software.objects.filter(provider=instance).annotate(
        vulnerabilities=Count('vulnerability'))

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'instance': instance,
        'instances': instances
    }

    return render(request, template_name, context)


def products(request):
    template_name = 'hotsite/products.html'
    title = 'Produtos'

    instances = Software.objects.all().annotate(
        vulnerabilities=Count('vulnerability'))

    context = {
        'title': title,
        'instances': instances
    }

    return render(request, template_name, context)


def product(request, pk):
    template_name = 'hotsite/product.html'

    instance = Software.objects.get(pk=pk)
    instances = Vulnerability.objects.filter(products=instance)

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'instances': instances,
    }

    return render(request, template_name, context)


def vulnerability(request, pk):
    template_name = 'hotsite/vulnerability.html'

    instance = Vulnerability.objects.get(pk=pk)

    context = {
        'head_title': instance.name + ' | ',
        'title': instance.name,
        'instance': instance
    }

    return render(request, template_name, context)


def mail_preview(request):
    instances = []
    provider_pos = 0
    template_name = 'panel/mail.html'

    today_str = date.today().strftime('%d/%m/%Y')
    yesterday = date.today() - timedelta(days=1)

    softwares_updated = Software.get_updated(date=yesterday)

    for instance in softwares_updated:
        if len(instances) == 0:
            instances.append({
                'provider': instance.provider.name,
                'softwares': []
            })

            last_provider_id = instance.provider.id

        if last_provider_id == instance.provider.id:
            instances[provider_pos]['softwares'].append({
                'name': instance.name,
                'version_stable': instance.version_stable
            })

        else:
            instances.append({
                'provider': instance.provider.name,
                'softwares': [{
                    'name': instance.name,
                    'version_stable': instance.version_stable
                }, ]
            })

            provider_pos += 1
            last_provider_id = instance.provider.id

    context = {
        'instances': instances,
        'date': today_str
    }

    return render(request, template_name, context)
