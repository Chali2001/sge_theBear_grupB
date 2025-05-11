// URL del endpoint de la API
const API_URL = "http://localhost:8000/pedidos/getAll";

// Función para obtener los datos de los usuarios
async function fetchInvoices() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const pedidos = await response.json(); // Convertimos la respuesta a JSON
        //console.log(facturas)
        displayInvoices(pedidos); // Mostramos los datos en la tabla
    } catch (error) {
        console.error("Error al obtener los pedidos:", error);
    }
}

// Función para mostrar los usuarios en la tabla
function displayInvoices(facturas) {
    const tableBody = document.querySelector("#pedidoTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de usuarios y creamos las filas de la tabla
    pedidos.forEach(pedido => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del usuario
        const idCell = document.createElement("td");
        idCell.textContent = pedido.Pedido.id;
        row.appendChild(idCell);

        const costoCell = document.createElement("td");
        costoCell.textContent = pedido.Pedido.id_cliente;
        row.appendChild(costoCell);

        const fechaCell = document.createElement("td");
        fechaCell.textContent = factura.Factura.id_producto;
        row.appendChild(fechaCell);

        const estadoCell = document.createElement("td");
        estadoCell.textContent = pedido.Pedido.estado;
        row.appendChild(estadoCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchInvoices);