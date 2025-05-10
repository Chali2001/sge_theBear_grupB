// URL del endpoint de la API
const API_URL = "http://localhost:8000/factura/";

// Función para obtener los datos de los usuarios
async function fetchInvoices() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const facturas = await response.json(); // Convertimos la respuesta a JSON
        displayInvoices(users); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener las facturas:", error);
    }
}

// Función para mostrar los usuarios en la tabla
function displayInvoices(facturas) {
    const tableBody = document.querySelector("#facturaTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de usuarios y creamos las filas de la tabla
    facturas.forEach(factura => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del usuario
        const idCell = document.createElement("td");
        idCell.textContent = factura.factura.id;
        row.appendChild(idCell);

        const costoCell = document.createElement("td");
        costoCell.textContent = factura.factura.costo;
        row.appendChild(nameCell);

        const fechaCell = document.createElement("td");
        fechaCell.textContent = factura.factura.fecha;
        row.appendChild(fechaCell);

        const estadoCell = document.createElement("td");
        estadoCell.textContent = factura.factura.estadoCell;
        row.appendChild(estadoCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchInvoices);