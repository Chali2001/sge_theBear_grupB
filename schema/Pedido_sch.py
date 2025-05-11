def pedido_schema(pedido) -> dict:
    return {
        "id": pedido.id,
        "id_cliente": pedido.id_cliente,
        "id_producto": pedido.id_producto,
        "estado": pedido.estado,
        "fecha": str(pedido.fecha)
    }

def pedidos_schema(pedidos) -> list[dict]:
    return [pedido_schema(p) for p in pedidos]