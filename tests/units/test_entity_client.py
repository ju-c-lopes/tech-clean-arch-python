from entities.cliente import Cliente

def test_create_new_client_success():
    # Given
    cliente = {
        "nome": "José",
        "email": "jose@email.com",
        "cpf": "11223344556"
    }
    
    # When
    novo_cliente = Cliente(nome=cliente["nome"], email=cliente["email"], cpf="11223344556")

    # Then
    assert novo_cliente.nome == "José"
    assert novo_cliente.email == "jose@email.com"
    assert novo_cliente.cpf == "11223344556"
