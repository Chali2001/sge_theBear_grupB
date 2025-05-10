def schema(emp) -> dict:
    send_emp = {"ID_empleado":emp["ID_empleado"],
                "nombre":emp["nombre"],
                "cargo":emp["cargo"],
                "ss":emp["ss"],
                "sueldo":emp["sueldo"],
                }
    return send_emp

def schemas(empleados) -> list[dict]:
    return [schema(empleado) for k,empleado in empleados.items()]


def schema_cliente(cli) -> dict:
    send_cli = {"ID_cliente:"cliente["ID_cliente"],
                    "nombre:"cliente["nombre"],
                    "telefono:"cliente["telefono"]
    }
    return send_cli

def schemas_cliente(clientes) -> list[dict]:
    return [schema(cliente) for k, cliente, in clientes.items()]
