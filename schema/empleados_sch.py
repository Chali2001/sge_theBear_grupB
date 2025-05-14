def empleado_schema(empleado) -> dict:
    response = {"empleado":empleado}
    return response

def empleados_schema(empleados) -> list[dict]:
    response = [empleado_schema(empleado) for empleado in empleados]
    return response