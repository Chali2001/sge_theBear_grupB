def punto_schema(punto) -> dict:
    response = {"Punto_Venta":punto}
    return response

def puntos_schema(puntos) -> list[dict]:
    response = [punto_schema(punto) for punto in puntos]
    return response