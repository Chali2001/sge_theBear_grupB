document.addEventListener('DOMContentLoaded', () => {
    const API_URL = 'http://localhost:8000';
    const clienteForm = document.getElementById('clienteForm');
    const messageDiv = document.getElementById('message');
    const clientesTableBody = document.querySelector('#clientesTable tbody');
    const formTitle = document.getElementById('formTitle');

    // Cargar clientes si estamos en la página de la tabla
    if (clientesTableBody) {
        fetchClientes();
    }

    // Manejar el formulario
    if (clienteForm) {
        const urlParams = new URLSearchParams(window.location.search);
        const editId = urlParams.get('id');
        if (editId) {
            loadClienteForEdit(editId);
            formTitle.textContent = 'Editar Client';
        }

        clienteForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const idCliente = document.getElementById('idCliente').value;
            const nombre = document.getElementById('nombre').value.trim();
            const telefono = document.getElementById('telefono').value.trim();
            const editId = document.getElementById('editId').value;

            const clienteData = { ID_cliente: parseInt(idCliente), nombre, telefono };

            try {
                let response;
                if (editId) {
                    response = await fetch(`${API_URL}/cliente/actualitzar/${editId}`, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(clienteData)
                    });
                } else {
                    response = await fetch(`${API_URL}/cliente/`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(clienteData)
                    });
                }

                if (response.ok) {
                    showMessage(editId ? 'Client actualitzat correctament!' : 'Client creat correctament!', 'success');
                    clienteForm.reset();
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

    // Cargar clientes
    async function fetchClientes() {
        try {
            const response = await fetch(`${API_URL}/clientes`);
            const clientes = await response.json();
            clientesTableBody.innerHTML = '';
            clientes.forEach(({ cliente }) => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${cliente.ID_cliente}</td>
                    <td>${cliente.nombre}</td>
                    <td>${cliente.telefono}</td>
                    <td>
                        <button class="action-btn" onclick="window.location.href='index_form.html?id=${cliente.ID_cliente}'">Editar</button>
                        <button class="action-btn" onclick="deleteCliente(${cliente.ID_cliente})">Eliminar</button>
                    </td>
                `;
                clientesTableBody.appendChild(row);
            });
        } catch (error) {
            console.error('Error al obtenir clients:', error);
        }
    }

    // Cargar datos para edición
    async function loadClienteForEdit(id) {
        try {
            const response = await fetch(`${API_URL}/clientes/${id}`);
            const data = await response.json();
            const cliente = data[0].cliente;
            document.getElementById('idCliente').value = cliente.ID_cliente;
            document.getElementById('nombre').value = cliente.nombre;
            document.getElementById('telefono').value = cliente.telefono;
            document.getElementById('editId').value = id;
        } catch (error) {
            console.error('Error al carregar client:', error);
        }
    }

    // Eliminar cliente
    window.deleteCliente = async function(id) {
        if (confirm('Segur que vols eliminar aquest client?')) {
            try {
                const response = await fetch(`${API_URL}/cliente/delete/${id}`, { method: 'DELETE' });
                if (response.ok) {
                    fetchClientes();
                } else {
                    alert('Error al eliminar el client');
                }
            } catch (error) {
                console.error('Error al eliminar client:', error);
            }
        }
    };

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = `message ${type}`;
    }
});