def factura(factura) -> dict:
    response = {"Facura":factura}
    return response

def facturas_schema(facturas) -> list[dict]:
    response = [factura(factura) for factura in facturas]
    return response