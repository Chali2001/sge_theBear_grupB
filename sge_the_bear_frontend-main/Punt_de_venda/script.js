// URL del endpoint de la API
const API_URL = "http://localhost:8000/puntoVenta/";

// Función para obtener los datos de los usuarios
async function fetchPunts() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const punts = await response.json(); // Convertimos la respuesta a JSON
        displayPunts(punts); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los puntos de venta:", error);
    }
}

// Función para mostrar los usuarios en la tabla
function displayPunts(punts) {
    const tableBody = document.querySelector("#puntTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de usuarios y creamos las filas de la tabla
    punts.forEach(punt => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del usuario
        const idCell = document.createElement("td");
        idCell.textContent = punt.punt.id;
        row.appendChild(idCell);

        const id_pedidoCell = document.createElement("td");
        id_pedidoCell.textContent = punt.punt.id_pedido;
        row.appendChild(id_pedidoCell);

        const reservaCell = document.createElement("td");
        reservaCell.textContent = punt.punt.reserva;
        row.appendChild(reservaCell);

        const id_factura = document.createElement("td");
        id_facturaCell.textContent = punt.punt.id_factura;
        row.appendChild(id_facturaCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchPunts);