def schema(emp) -> dict:
    send_emp = {"ID_empleado":emp["ID_empleado"],
                "nombre":emp["nombre"],
                "cargo":emp["cargo"],
                "ss":emp["ss"],
                "sueldo":emp["sueldo"],
                }
    return send_emp

def schemas(empleados) -> list[dict]:
    return [schema(empleado) for k, empleado in empleados.items()]
