def factura_schema(factura) -> dict:
    response = {"Factura":factura}
    return response

def facturas_schema(facturas) -> list[dict]:
    response = [factura_schema(factura) for factura in facturas]
    return response