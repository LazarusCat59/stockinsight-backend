from django.core.management.base import BaseCommand, CommandError
from restapi.models import Stock, AuditDetail, StockType, Computer
import datetime
import csv

def validate_row(row, prev_row):
    validated_row = []
    for i in range(len(row)):
        if row[i] == '"':
            validated_row.append(prev_row[i])
            continue

        validated_row.append(row[i])

    return validated_row

def create_computer(bill_no, purchase_date, item_code, description):
    kb = Stock.objects.create(name="Generic Keyboard", bill_no=bill_no, item_code=item_code, purchase_date=purchase_date)
    mouse = Stock.objects.create(name="Generic Mouse", bill_no=bill_no, item_code=item_code, purchase_date=purchase_date)
    cpu = Stock.objects.create(name="Generic CPU", bill_no=bill_no, item_code=item_code, purchase_date=purchase_date)
    monitor = Stock.objects.create(name="Generic Monitor", bill_no=bill_no, item_code=item_code, purchase_date=purchase_date)

    return Computer.objects.create(keyboard=kb, mouse=mouse, cpu=cpu, monitor=monitor, description=description)

class Command(BaseCommand):
    help = "Adds data from a csv file into database"

    def add_arguments(self, parser):
        parser.add_argument("filename", type=str)

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']

        rows = []

        with open(filename, "r") as file:
            rows = list(csv.reader(file))

        temp_row = rows[1]
        for row in rows[1:]:
            # print(row)
            validated_row = validate_row(row, temp_row)
            temp_row = validated_row

            name = validated_row[1]
            bill_no = validated_row[3].split('.')[0].strip()
            purchase_date = datetime.datetime.strptime(validated_row[3].split('.')[1].strip(), "%d/%b/%Y").date()
            description = validated_row[9]
            item_code = validated_row[2]

            # self.stdout.write(f"{bill_no} {purchase_date} {description} {item_code}")

            if(name == "Computer"):
                create_computer(bill_no, purchase_date, item_code, description)
            else:
                Stock.objects.create(name=name, bill_no=bill_no, purchase_date=purchase_date, item_code=item_code, description=description)
