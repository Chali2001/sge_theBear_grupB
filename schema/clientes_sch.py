def cliente_schema(cliente) -> dict:
    response = {"cliente":cliente}
    return response

def clientes_schema(clientes) -> list[dict]:
    response = [cliente_schema(cliente) for cliente in clientes]
    return response

