from collections import Counter
from datetime import date


class SimpleReport:
    def generate(products):
        manufacturing_date = [
            product["data_de_fabricacao"] for product in products
        ]
        today = date.fromisoformat(date.today().isoformat())
        validate_date = [
            product["data_de_validade"] for product in products
            if date.fromisoformat(product["data_de_validade"]) > today
        ]
        company_names = [product["nome_da_empresa"] for product in products]
        oldest_product = min(manufacturing_date)
        newest_product = min(validate_date)
        company_frequency = Counter(company_names)
        more_repeated_company = [
            product
            for product in company_frequency.keys()
            if company_frequency[product] == max(company_frequency.values())
        ]
        return (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {newest_product}\n"
            f"Empresa com mais produtos: {more_repeated_company[0]}"
        )
