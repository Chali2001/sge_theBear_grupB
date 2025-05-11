document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('facturaUpdateForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari

        const idInput = document.getElementById('id').value;
        const id = idInput ? parseInt(idInput) : null;

        if (!id) {
            showMessage('Por favor, ingresa un ID válido', 'error');
            return;
        }
        const estado = document.getElementById('estado').value.trim();

         try {
            // Enviar dades al servidor amb body JSON
            const response = await fetch('http://localhost:8000/factura/update/estado/'+id, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    id: id,
                    estado: estado
                })
            });

            const data = await response.json();

            if (response.ok) {
                showMessage('Factura actualizada correctament!', 'success');
                form.reset(); // Netejar el formulari
            } else {
                showMessage(`Error: ${data.message || data.detail || 'Error desconegut'}`, 'error');
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