document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('puntDeleteForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener el ID del punto de venta a eliminar
        const idInput = document.getElementById('id').value;
        const id = idInput ? parseInt(idInput) : null;
        if (!id) {
            showMessage('Por favor, ingresa un ID válido', 'error');
            return;
        }

        try {
            // Enviar solicitud DELETE al servidor
                const response = await fetch('http://localhost:8000/puntoVenta/delete/' + id, {
                method: 'DELETE',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            });

            const data = await response.json();

            if (response.ok) {
                showMessage('Punto de venta eliminado correctamente!', 'success');
                form.reset();  // Limpiar el formulario
            } else {
                showMessage(`Error: ${data.detail || 'Error desconocido'}`, 'error');
            }
        } catch (error) {
            showMessage(`Error de conexión: ${error.message}`, 'error');
        }
    });

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = 'message ' + type;
    }
});
