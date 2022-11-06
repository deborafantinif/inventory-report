import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def handle_read_file(path):
        with open(path, "r") as file_products:
            products = ""
            if "csv" in path:
                products = list(
                    csv.DictReader(file_products, delimiter=",", quotechar='"')
                )
            elif "json" in path:
                products = json.load(file_products)
            elif "xml" in path:
                products = xmltodict.parse(file_products.read())["dataset"][
                    "record"
                ]
            return products

    @classmethod
    def import_data(cls, path, type_report):
        products = cls.handle_read_file(path)
        if type_report == "simples":
            return SimpleReport.generate(products)
        if type_report == "completo":
            return CompleteReport.generate(products)
