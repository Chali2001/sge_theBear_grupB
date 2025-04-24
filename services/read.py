from schema import read_sch


def registre():
    empleados = {
        {
            "ID_empleado": 1,
            "nombre": "Laura Martínez",
            "cargo": "Analista",
            "ss": "12345678A",
            "sueldo": 28000
        },
        {
            "ID_empleado": 2,
            "nombre": "Carlos Gómez",
            "cargo": "Desarrollador",
            "ss": "87654321B",
            "sueldo": 32000
        },
        {
            "ID_empleado": 3,
            "nombre": "Sofía Ruiz",
            "cargo": "Diseñadora UX",
            "ss": "45678912C",
            "sueldo": 30000
        },
        {
            "ID_empleado": 4,
            "nombre": "Miguel Torres",
            "cargo": "Jefe de Proyecto",
            "ss": "98765432D",
            "sueldo": 45000
        },
        {
            "ID_empleado": 5,
            "nombre": "Andrea López",
            "cargo": "Administrativa",
            "ss": "11223344E",
            "sueldo": 25000
        }

    }
    return read_sch.schemas(empleados)
