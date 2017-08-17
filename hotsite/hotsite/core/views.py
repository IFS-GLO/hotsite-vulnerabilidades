from django.shortcuts import render


def index(request):
    template_name = 'hotsite/index.html'

    tab = request.GET.get('tab', '')

    if tab == '':
        title = 'Vulnerabilidades'

    elif tab == 'provider':
        title = 'Fornecedores'

    elif tab == 'software':
        title = 'Produtos'

    context = {
        'title': title
    }

    return render(request, template_name, context)
