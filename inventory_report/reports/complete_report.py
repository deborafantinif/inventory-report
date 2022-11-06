from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, products):
        first_part = super().generate(products)
        company_names = [product["nome_da_empresa"] for product in products]
        company_frequency = Counter(company_names)
        phrases = ""
        for company in company_frequency.keys():
            phrase = f"- {company}: {company_frequency[company]}\n"
            phrases += phrase
        return (
            f"{first_part}\n" f"Produtos estocados por empresa:\n" f"{phrases}"
        )
