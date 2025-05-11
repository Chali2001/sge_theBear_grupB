document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('facturaForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const costo = parseFloat(document.getElementById('costo').value);
        const fecha = document.getElementById('fecha').value.trim();
        const estado = document.getElementById('estado').value.trim();

         try {
            // Enviar dades al servidor amb body JSON
            const response = await fetch('http://localhost:8000/factura/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    costo: costo,
                    fecha: fecha,
                    estado: estado
                })
            });

            const data = await response.json();

            if (response.ok) {
                showMessage('Factura creat correctament!', 'success');
                form.reset(); // Netejar el formulari
            } else {
                showMessage(`Error: ${data.detail || 'Error desconegut'}`, 'error');
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