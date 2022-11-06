from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "calendar",
        "register LTDA",
        "12-02-2002",
        "29-12-2999",
        "0002456",
        "local seco, sem expor ao sol",
    )

    response_product = "O produto calendar fabricado em 12-02-2002 por register \
LTDA com validade até 29-12-2999 precisa ser armazenado local seco, sem \
expor ao sol."

    assert product.__repr__() == response_product
