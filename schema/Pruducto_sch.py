def producto_schema(producto) -> dict:
    return {
        "id": producto.id,
        "name": producto.name,
        "stock": producto.stock,
        "precio": producto.precio
    }

def productos_schema(productos) -> list[dict]:
    return [producto_schema(p) for p in productos]