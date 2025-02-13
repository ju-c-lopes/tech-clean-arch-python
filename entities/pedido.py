from typing import List

from .cliente import Cliente
from .produto import Produto


class Pedido:
    def __init__(
        self,
        cliente: Cliente,
        produtos: List[Produto],
        personalizacao: str = None,
        codigo_do_pedido: str = None,
        status: str = "PENDENTE",
        total: float = 0.0,
    ):
        self.cliente = cliente
        self.produtos = produtos
        self.personalizacao = personalizacao
        self.codigo_do_pedido = codigo_do_pedido
        self.status = status
        self.total = self.calcular_total()

    def __repr__(self):
        return f"""
Pedido(cliente={self.cliente}
produtos={[produto for produto in self.produtos]}
OBSERVAÇÃO: {self.personalizacao}
COD: {self.codigo_do_pedido}
Total: R$ {self.total:.2f}
status={self.status})
"""

    def calcular_total(self):
        if not len(self.produtos) or len(self.produtos) == 0:
            raise ValueError("Não é possível criar um pedido sem produtos!")
        try:
            return sum(produto.preco for produto in self.produtos)
        except Exception:
            pass
