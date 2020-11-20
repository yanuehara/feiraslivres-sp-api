from django.core.management.base import BaseCommand, CommandError
from feiraapi.models import Feira
import csv

class Command(BaseCommand):
    # Defines importcsv command
    help = 'Import feiras from the csv'

    def add_arguments(self, parser):
        # Add csv_file as argument
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        # Handle the new command
        with open(options['csv_file']) as f:
            # Open file
            
            feiras_as_dict = csv.DictReader(f)
            feiras_list_of_dict = list(feiras_as_dict)
            # Read file as a list of dicts

            feiras = [
                Feira(
                    id = row['ID'],
                    long = row['LONG'],
                    lat = row['LAT'],
                    setcens = row['SETCENS'],
                    areap = row['AREAP'],
                    coddist = row['CODDIST'],
                    distrito = row['DISTRITO'],
                    codsubpref = row['CODSUBPREF'],
                    subpref = row['SUBPREFE'],
                    regiao5 = row['REGIAO5'],
                    regiao8 = row['REGIAO8'],
                    nome_feira = row['NOME_FEIRA'],
                    registro = row['REGISTRO'],
                    logradouro = row['LOGRADOURO'],
                    numero = ('' if (row['NUMERO']=='' or row['NUMERO']=='S/N') else row['NUMERO'].split('.')[0] ),
                    bairro = row['BAIRRO'],
                    referencia = row['REFERENCIA'],
                )
                for row in feiras_list_of_dict
            ]
            # For each item in the list create a Feira object for them

            msg = Feira.objects.bulk_create(feiras)
            # Bulk create the objects in the DB

            self.stdout.write(self.style.SUCCESS('Successfully run created the following Feiras from CSV %s') % str(msg))