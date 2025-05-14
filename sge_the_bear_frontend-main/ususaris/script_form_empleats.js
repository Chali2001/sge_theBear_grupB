document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('empleatForm');
    const messageDiv = document.getElementById('message');
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');

    if (id) {
        document.querySelector('h1').textContent = 'Editar Empleat';
        form.querySelector('button[type="submit"]').textContent = 'Actualitzar Empleat';
        fetchEmpleat(id);
    }

    async function fetchEmpleat(id) {
        try {
            const response = await fetch(`http://localhost:8000/empleados/${id}`);
            if (response.ok) {
                const data = await response.json();
                const empleat = data.empleado;
                document.getElementById('id_empleat').value = empleat.ID_empleado;
                document.getElementById('nom').value = empleat.nombre;
                document.getElementById('carrec').value = empleat.cargo;
                document.getElementById('ss').value = empleat.ss;
                document.getElementById('sou').value = empleat.sueldo;
                document.getElementById('id_empleat').disabled = true;
            } else {
                showMessage('Error al carregar l\'empleat', 'error');
            }
        } catch (error) {
            showMessage(`Error de connexió: ${error.message}`, 'error');
        }
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const id_empleat = parseInt(document.getElementById('id_empleat').value);
        const nom = document.getElementById('nom').value.trim();
        const carrec = document.getElementById('carrec').value.trim();
        const ss = parseInt(document.getElementById('ss').value);
        const sou = parseInt(document.getElementById('sou').value);

        const data = {
            ID_empleado: id_empleat,
            nombre: nom,
            cargo: carrec,
            ss: ss,
            sueldo: sou
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
                if (id) window.location.href = 'index_table_empleats.html';
            } else {
                const errorData = await response.json();
                showMessage.Host(`Error: ${errorData.detail || 'Error desconegut'}`, 'error');
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