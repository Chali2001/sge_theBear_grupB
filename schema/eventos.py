def evento_dict(evento) -> dict:
    return {"Evento": evento}

def eventos_schema(eventos) -> list[dict]:
    return [evento_dict(evento) for evento in eventos]