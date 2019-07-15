from datetime import date, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.template import Context
from django.template.loader import render_to_string

from hotsite.core.utils import send_email
from hotsite.catalog.models import Software


class Command(BaseCommand):
    title = 'Process Emails'
    help = 'Sends emails'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
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

        send_email(
            context,
            ['grp-ctis@ifs.edu.br', 'raphael.fontes@ifs.edu.br'],
            f'Resumo de Alerta de Segurança - {today_str}',
            template_name
        )

        self.stdout.write(self.style.SUCCESS('Successfully emails sent!'))
