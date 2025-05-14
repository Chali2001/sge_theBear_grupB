document.addEventListener('DOMContentLoaded', () => {
    const API_URL = 'http://localhost:8000';
    const empleadoForm = document.getElementById('empleadoForm');
    const messageDiv = document.getElementById('message');
    const empleadosTableBody = document.querySelector('#empleadosTable tbody');
    const formTitle = document.getElementById('formTitle');

    // Cargar empleados si estamos en la página de la tabla
    if (empleadosTableBody) {
        fetchEmpleados();
    }

    // Manejar el formulario
    if (empleadoForm) {
        const urlParams = new URLSearchParams(window.location.search);
        const editId = urlParams.get('id');
        if (editId) {
            loadEmpleadoForEdit(editId);
            formTitle.textContent = 'Editar Empleat';
        }

        empleadoForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const idEmpleado = document.getElementById('idEmpleado').value;
            const nombre = document.getElementById('nombre').value.trim();
            const cargo = document.getElementById('cargo').value.trim();
            const ss = document.getElementById('ss').value;
            const sueldo = document.getElementById('sueldo').value;
            const editId = document.getElementById('editId').value;

            const empleadoData = {
                ID_empleado: parseInt(idEmpleado),
                nombre,
                cargo,
                ss: parseInt(ss),
                sueldo: parseInt(sueldo)
            };

            try {
                let response;
                if (editId) {
                    response = await fetch(`${API_URL}/empleado/actualitzar/${editId}`, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(empleadoData)
                    });
                } else {
                    response = await fetch(`${API_URL}/empleado/`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(empleadoData)
                    });
                }

                if (response.ok) {
                    showMessage(editId ? 'Empleat actualitzat correctament!' : 'Empleat creat correctament!', 'success');
                    empleadoForm.reset();
                    document.getElementById('editId').value = '';
                    setTimeout(() => window.location.href = 'index_table.html', 1000);
                } else {
                    const data = await response.json();
                    showMessage(`Error: ${data.detail || 'Error desconegut'}`, 'error');
                }
            } catch (error) {
                showMessage(`Error de connexió: ${error.message}`, 'error');
            }
        });
    }

    // Cargar empleados
    async function fetchEmpleados() {
        try {
            const response = await fetch(`${API_URL}/empleados`);
            const empleados = await response.json();
            empleadosTableBody.innerHTML = '';
            empleados.forEach(({ empleado }) => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${empleado.ID_empleado}</td>
                    <td>${empleado.nombre}</td>
                    <td>${empleado.cargo}</td>
                    <td>${empleado.ss}</td>
                    <td>${empleado.sueldo}</td>
                    <td>
                        <button class="action-btn" onclick="window.location.href='index_form.html?id=${empleado.ID_empleado}'">Editar</button>
                        <button class="action-btn" onclick="deleteEmpleado(${empleado.ID_empleado})">Eliminar</button>
                    </td>
                `;
                empleadosTableBody.appendChild(row);
            });
        } catch (error) {
            console.error('Error al obtenir empleats:', error);
        }
    }

    // Cargar datos para edición
    async function loadEmpleadoForEdit(id) {
        try {
            const response = await fetch(`${API_URL}/empleados/${id}`);
            const data = await response.json();
            const empleado = data[0].empleado;
            document.getElementById('idEmpleado').value = empleado.ID_empleado;
            document.getElementById('nombre').value = empleado.nombre;
            document.getElementById('cargo').value = empleado.cargo;
            document.getElementById('ss').value = empleado.ss;
            document.getElementById('sueldo').value = empleado.sueldo;
            document.getElementById('editId').value = id;
        } catch (error) {
            console.error('Error al carregar empleat:', error);
        }
    }

    // Eliminar empleado
    window.deleteEmpleado = async function(id) {
        if (confirm('Segur que vols eliminar aquest empleat?')) {
            try {
                const response = await fetch(`${API_URL}/empleado/delete/${id}`, { method: 'DELETE' });
                if (response.ok) {
                    fetchEmpleados();
                } else {
                    alert('Error al eliminar l\'empleat');
                }
            } catch (error) {
                console.error('Error al eliminar empleat:', error);
            }
        }
    };

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = `message ${type}`;
    }
});