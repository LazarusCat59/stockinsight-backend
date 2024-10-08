from django.core.management.base import BaseCommand, CommandError
from restapi.models import Stock, AuditDetail, Computer
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

def create_computer(bill_no, purchase_date, item_code, description, location):
    kb = Stock.objects.create(name="Generic Keyboard", bill_no=bill_no, item_code=item_code, purchase_date=purchase_date, location=location)
    mouse = Stock.objects.create(name="Generic Mouse", bill_no=bill_no, item_code=item_code, purchase_date=purchase_date, location=location)
    cpu = Stock.objects.create(name="Generic CPU", bill_no=bill_no, item_code=item_code, purchase_date=purchase_date, location=location)
    monitor = Stock.objects.create(name="Generic Monitor", bill_no=bill_no, item_code=item_code, purchase_date=purchase_date, location=location)

    return Computer.objects.create(name="Computer", keyboard=kb, mouse=mouse, cpu=cpu, monitor=monitor, description=description, location=location)

class Command(BaseCommand):
    help = "Adds data from a csv file into database"

    def add_arguments(self, parser):
        parser.add_argument("filename", type=str)
        parser.add_argument("location", nargs='?', type=str, default="LAB_1")

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        location = kwargs['location']

        rows = []

        self.stdout.write(f"Opening {filename}")
        with open(filename, "r") as file:
            rows = list(csv.reader(file))

        self.stdout.write("Processing rows..")
        temp_row = rows[1]
        for row in rows[1:]:
            validated_row = validate_row(row, temp_row)
            temp_row = validated_row

            name = validated_row[1].strip()
            bill_no = validated_row[3].split('.')[0].strip()
            purchase_date = datetime.datetime.strptime(validated_row[3].split('.')[1].strip(), "%d/%b/%Y").date()
            description = validated_row[9].strip()
            item_code = validated_row[2].strip()

            # self.stdout.write(f"{bill_no} {purchase_date} {description} {item_code} {location}")

            if(name == "Computer"):
                create_computer(bill_no, purchase_date, item_code, description, location)
            else:
                Stock.objects.create(name=name, bill_no=bill_no, purchase_date=purchase_date, item_code=item_code, description=description, location=location)

        self.stdout.write("Import complete!")
