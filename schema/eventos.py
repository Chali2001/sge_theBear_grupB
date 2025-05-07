def evento(evento) -> dict:
    response = {"Evento": evento}
    return response

def eventos_schema(eventos) -> list[dict]:
    response = [evento(evento) for evento in eventos]
    return response