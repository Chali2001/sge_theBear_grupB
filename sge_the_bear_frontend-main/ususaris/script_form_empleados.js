document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('empleadoForm');
    const messageDiv = document.getElementById('message');
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');

    if (id) {
        // Modo edición
        document.querySelector('h1').textContent = 'Editar Empleat';
        form.querySelector('button[type="submit"]').textContent = 'Actualitzar Empleat';
        fetchEmpleado(id);
    }

    async function fetchEmpleado(id) {
        try {
            const response = await fetch(`http://localhost:8000/empleados/${id}`);
            if (response.ok) {
                const data = await response.json();
                const empleado = data.empleado;
                document.getElementById('id_empleado').value = empleado.ID_empleado;
                document.getElementById('nombre').value = empleado.nombre;
                document.getElementById('cargo').value = empleado.cargo;
                document.getElementById('ss').value = empleado.ss;
                document.getElementById('sueldo').value = empleado.sueldo;
                document.getElementById('id_empleado').disabled = true; // Evitar modificar ID
            } else {
                showMessage('Error al carregar l\'empleat', 'error');
            }
        } catch (error) {
            showMessage(`Error de connexió: ${error.message}`, 'error');
        }
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const id_empleado = parseInt(document.getElementById('id_empleado').value);
        const nombre = document.getElementById('nombre').value.trim();
        const cargo = document.getElementById('cargo').value.trim();
        const ss = parseInt(document.getElementById('ss').value);
        const sueldo = parseInt(document.getElementById('sueldo').value);

        const data = {
            ID_empleado: id_empleado,
            nombre: nombre,
            cargo: cargo,
            ss: ss,
            sueldo: sueldo
        };

        try {
            const url = id ? `http://localhost:8000/empleado/actualitzar/${id}` : 'http://localhost:8000/empleado/';
            const method = id ? 'PUT' : 'POST';

            const response = await fetch(url, {
                method: method,
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                showMessage(id ? 'Empleat actualitzat correctament!' : 'Empleat creat correctament!', 'success');
                form.reset();
                if (id) window.location.href = 'index_table_empleados.html';
            } else {
                const errorData = await response.json();
                showMessage(`Error: ${errorData.detail || 'Error desconegut'}`, 'error');
            }
        } catch (error) {
            showMessage(`Error de connexió: ${error.message}`, 'error');
        }
    });

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = 'message ' + type;
    }
});