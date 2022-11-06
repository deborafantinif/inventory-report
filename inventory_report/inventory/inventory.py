import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type_report):
        with open(path, 'r') as file_products:
            products = list(csv.DictReader(
                file_products, delimiter=",", quotechar='"'
            ))
            if type_report == "simples":
                return SimpleReport.generate(products)
            if type_report == "completo":
                return CompleteReport.generate(products)
