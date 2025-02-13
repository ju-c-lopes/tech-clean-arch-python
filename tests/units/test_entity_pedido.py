from entities.cliente import Cliente
from entities.pedido import Pedido
from entities.produto import Produto


def test_create_new_pedido_success():
    # Given
    cliente = Cliente(
        nome="José da Silva",
        email="jose@email.com",
        cpf="11223344556"
    )
    produtos = [Produto(
        id="1",
        nome="X-burguer",
        descricao="Pão, carne, queijo e salada",
        categoria="LANCHE",
        preco=20.0,
        disponivel=True
    ), Produto(
        id="2",
        nome="Coca-cola",
        descricao="Lata 350ml",
        categoria="BEBIDA",
        preco=5.0,
        disponivel=True
    )]

    # When
    pedido = Pedido(
        cliente=cliente,
        produtos=produtos,
        personalizacao="Sem cebola",
        codigo_do_pedido="123456"
    )

    # Then
    assert pedido.cliente == cliente
    assert pedido.produtos == produtos
    assert pedido.personalizacao == "Sem cebola"
    assert pedido.codigo_do_pedido == "123456"
    assert pedido.status == "PENDENTE"
    assert pedido.calcular_total() == 25.0
    assert str(pedido) == """
Pedido(cliente=Cliente(nome=José da Silva, email=jose@email.com, cpf=11223344556)
produtos=[
LANCHE:
    X-burguer
    Preço = R$ 20.00
, 
BEBIDA:
    Coca-cola
    Preço = R$ 5.00
]
OBSERVAÇÃO: Sem cebola
COD: 123456
Total: R$ 25.00
status=PENDENTE)
"""


def test_create_new_pedido_without_products():
    # Given
    cliente = Cliente(
        nome="José da Silva",
        email="jose@email.com",
        cpf="11223344556"
    )
    produtos = []

    # When
    try:
        Pedido(
            cliente=cliente,
            produtos=produtos,
            personalizacao="Sem cebola",
            codigo_do_pedido="123456"
        )
    except ValueError as error:
        # Then
        assert str(error) == "Não é possível criar um pedido sem produtos!"
