from entities.produto import Produto


def test_create_new_produto_success():
    # Given
    produto = Produto(
        id="1",
        nome="X-burguer",
        descricao="Pão, carne, queijo e salada",
        categoria="LANCHE",
        preco=20.0,
        disponivel=True
    )

    # Then
    assert produto._id == "1"
    assert produto.nome == "X-burguer"
    assert produto.descricao == "Pão, carne, queijo e salada"
    assert produto.categoria == "LANCHE"
    assert produto.preco == 20.0
    assert produto.disponivel is True
    assert str(produto) == """
LANCHE:
    X-burguer
    Preço = R$ 20.00
"""


def test_create_new_produto_fail():
    # Given
    try:
        Produto(
            id="1",
            nome="X-burguer",
            descricao="Pão, carne, queijo e salada",
            categoria="LANCHE",
            preco=-20.0,
            disponivel=True
        )
    except ValueError as error:
        assert str(error) == "Preço do produto não pode ser negativo!"
