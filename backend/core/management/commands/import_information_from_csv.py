import csv
import os

from django.core.management.base import BaseCommand

from api.serializers.rolling_stock.rolling_stock_serializer import RollingStockSerializer
from api.serializers.rolling_stock.rolling_stock_information_serializer import RollingStockInformationSerializer
from core.models.information.information_model import Information
from core.models.rolling_stock.rolling_stock_information_model import RollingStockInformation
from core.models.user.user_model import User


class Command(BaseCommand):
    help = 'Import a list of information from a CSV file'
    indexes = {}

    def __init__(self, *args, **kwargs):
        self.options = {}
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help="The CSV filepath to import (required).")
        parser.add_argument('--verbose', type=bool, default=False, help="Increase text output. Useful for debugging.")

    def handle(self, *args, **options):
        filepath = self.options['filepath']

        if not os.path.exists(filepath):
            self.stdout.write(
                self.style.WARNING('The CSV file "{}" was not found!'.format(filepath))
            )
            return

        information_list = []
        required_fields = ['item_type', 'name', 'information_text', 'references']
        with open(filepath, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.DictReader(csvfile, dialect=dialect)
            for row in reader:
                if any([field not in row for field in required_fields]):
                    self.stdout.write(
                        self.style.WARNING('The CSV line #{} does not contain all the required fields {}!'.format(
                            reader.line_num,
                            ', '.join(required_fields)
                        ))
                    )
                    return
                information_list.append(row)

        for row in information_list:
            self.stdout.write('Saving info for rolling stock named {}...'.format(row['name']))
            self.add_information(row['item_type'], row['name'], row['information_text'], row['references'])

        self.stdout.write(self.style.SUCCESS('{} information entries were persisted on the database!'.format(
            len(information_list)
        )))

    def add_information(self, item_type: str, name: str, information_text: str, references: str):
        user = User.objects.get(username=os.environ['SYSTEM_USER_NAME'])

        rolling_stock = RollingStockSerializer.get_or_create_from_name_and_type(
            name, item_type
        )

        if RollingStockInformationSerializer.check_if_info_exists(rolling_stock, information_text):
            self.stdout.write(
                self.style.WARNING('The information "{}" is already present at database!'.format(information_text))
            )
            return

        information = Information.objects.get_or_create(
            author=user,
            content=information_text,
            status=Information.InformationStatus.DISCUSSION,
            references=references,
        )
        information.save()

        self.stdout.write("Information ID: {}".format(information.id))

        rolling_stock_information, created = RollingStockInformation.objects.get_or_create(
            rolling_stock=rolling_stock,
            information=information
        )
        self.stdout.write("RollingStockInformation ID: {}".format(rolling_stock_information.id))
