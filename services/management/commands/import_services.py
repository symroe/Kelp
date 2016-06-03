import json
import glob


from django.core.management.base import BaseCommand

from services.models import Service, Provider


class Command(BaseCommand):


    def handle(self, **options):
        for file_path in glob.glob('scraper/data/*.json'):
            data = json.loads(open(file_path).read())
            provider, _ = Provider.objects.get_or_create(
                name=data['company_name']
            )

            service, _ = Service.objects.update_or_create(
                service_id=data['service_id'],
                defaults={
                    'service_name': data['service_name'],
                    'raw_html': data['page_content'],
                    'provider': provider
                }
            )

