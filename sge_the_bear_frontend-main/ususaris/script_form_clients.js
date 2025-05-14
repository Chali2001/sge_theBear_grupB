document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('clientForm');
    const messageDiv = document.getElementById('message');
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');

    if (id) {
        document.querySelector('h1').textContent = 'Editar Client';
        form.querySelector('button[type="submit"]').textContent = 'Actualitzar Client';
        fetchClient(id);
    }

    async function fetchClient(id) {
        try {
            const response = await fetch(`http://localhost:8000/clientes/${id}`);
            if (response.ok) {
                const data = await response.json();
                const client = data.cliente;
                document.getElementById('id_client').value = client.ID_cliente;
                document.getElementById('nom').value = client.nombre;
                document.getElementById('telefon').value = client.telefono;
                document.getElementById('id_client').disabled = true;
            } else {
                showMessage('Error al carregar el client', 'error');
            }
        } catch (error) {
            showMessage(`Error de connexió: ${error.message}`, 'error');
        }
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const id_client = parseInt(document.getElementById('id_client').value);
        const nom = document.getElementById('nom').value.trim();
        const telefon = document.getElementById('telefon').value.trim();

        const data = {
            ID_cliente: id_client,
            nombre: nom,
            telefono: telefon
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
                if (id) window.location.href = 'index_table_clients.html';
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