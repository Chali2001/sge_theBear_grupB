// URL del endpoint de la API
const API_URL = "http://localhost:8000/puntoVenta/getAll";

// Función para obtener los datos de los usuarios
async function fetchPunts() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const punts = await response.json(); // Convertimos la respuesta a JSON
        console.log(punts);
        displayPunts(punts); // Mostramos los datos en la tabla
    } catch (error) {
        console.error("Error al obtener los puntos de venta:", error);
    }
}

// Función para mostrar los usuarios en la tabla
function displayPunts(punts) {
    const tableBody = document.querySelector("#puntTable tbody");
    tableBody.innerHTML = "";

    punts.forEach(punt => {
        const row = document.createElement("tr");

        const idCell = document.createElement("td");
        idCell.textContent = punt["Punto_Venta"].id;
        row.appendChild(idCell);

        const id_pedidoCell = document.createElement("td");
        id_pedidoCell.textContent = punt["Punto_Venta"].id_pedido;
        row.appendChild(id_pedidoCell);

        const reservaCell = document.createElement("td");
        reservaCell.textContent = punt["Punto_Venta"].reserva ? 'Sí' : 'No';
        row.appendChild(reservaCell);

        const id_facturaCell = document.createElement("td");
        id_facturaCell.textContent = punt["Punto_Venta"].id_factura ?? '-';
        row.appendChild(id_facturaCell);

        tableBody.appendChild(row);
    });
}


// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchPunts);