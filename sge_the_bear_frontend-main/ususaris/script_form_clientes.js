document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('clienteForm');
    const messageDiv = document.getElementById('message');
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');

    if (id) {
        // Modo edición
        document.querySelector('h1').textContent = 'Editar Client';
        form.querySelector('button[type="submit"]').textContent = 'Actualitzar Client';
        fetchCliente(id);
    }

    async function fetchCliente(id) {
        try {
            const response = await fetch(`http://localhost:8000/clientes/${id}`);
            if (response.ok) {
                const data = await response.json();
                const cliente = data.cliente;
                document.getElementById('id_cliente').value = cliente.ID_cliente;
                document.getElementById('nombre').value = cliente.nombre;
                document.getElementById('telefono').value = cliente.telefono;
                document.getElementById('id_cliente').disabled = true;
            } else {
                showMessage('Error al carregar el client', 'error');
            }
        } catch (error) {
            showMessage(`Error de connexió: ${error.message}`, 'error');
        }
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const id_cliente = parseInt(document.getElementById('id_cliente').value);
        const nombre = document.getElementById('nombre').value.trim();
        const telefono = document.getElementById('telefono').value.trim();

        const data = {
            ID_cliente: id_cliente,
            nombre: nombre,
            telefono: telefono
        };

        try {
            const url = id ? `http://localhost:8000/cliente/actualitzar/${id}` : 'http://localhost:8000/cliente/';
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
                showMessage(id ? 'Client actualitzat correctament!' : 'Client creat correctament!', 'success');
                form.reset();
                if (id) window.location.href = 'index_table_clientes.html';
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