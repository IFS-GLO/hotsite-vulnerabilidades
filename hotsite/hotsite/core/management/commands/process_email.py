from django.core.management.base import BaseCommand, CommandError
from hotsite.core.utils import send_email


class Command(BaseCommand):
    title = 'Process emails'
    help = 'Sends emails'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        send_email(['raphael.fontes@ifs.edu.br'],
                   'Resumo de Alerta de Segurança - 09/07/2019', 'panel/mail.html')
        self.stdout.write(self.style.SUCCESS('Successfully emails sent!'))
