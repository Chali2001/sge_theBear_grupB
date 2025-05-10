document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('puntForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const id_pedido = parseInt(document.getElementById('id_pedido').value);
        const reserva = document.getElementById('reserva').value.trim();
        const id_factura = parseInt(document.getElementById('id_factura').value);

         try {
            // Enviar dades al servidor amb body JSON
            const response = await fetch('http://localhost:8000/puntoVenta/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    id_pedido: id_pedido,
                    reserva: reserva,
                    id_factura: id_factura
                })
            });

            if (response.ok) {
                showMessage('Punt de venda creat correctament!', 'success');
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