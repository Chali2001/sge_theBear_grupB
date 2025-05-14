const API_URL = "http://localhost:8000/clientes";

async function fetchClients() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const clients = await response.json();
        displayClients(clients);
    } catch (error) {
        console.error("Error al obtenir els clients:", error);
    }
}

function displayClients(clients) {
    const tableBody = document.querySelector("#clientsTable tbody");
    tableBody.innerHTML = "";

    clients.forEach(data => {
        const client = data.cliente;
        const row = document.createElement("tr");

        const idCell = document.createElement("td");
        idCell.textContent = client.ID_cliente;
        row.appendChild(idCell);

        const nameCell = document.createElement("td");
        nameCell.textContent = client.nombre;
        row.appendChild(nameCell);

        const telefonCell = document.createElement("td");
        telefonCell.textContent = client.telefono;
        row.appendChild(telefonCell);

        const actionsCell = document.createElement("td");
        actionsCell.innerHTML = `
            <button aria-label="Editar client ${client.nombre}" onclick="editClient(${client.ID_cliente})">Editar</button>
            <button aria-label="Eliminar client ${client.nombre}" onclick="deleteClient(${client.ID_cliente})">Eliminar</button>
        `;
        row.appendChild(actionsCell);

        tableBody.appendChild(row);
    });
}

function editClient(id) {
    window.location.href = `index_form_clients.html?id=${id}`;
}

async function deleteClient(id) {
    if (confirm("Estàs segur d'eliminar aquest client?")) {
        try {
            const response = await fetch(`http://localhost:8000/cliente/delete/${id}`, {
                method: 'DELETE'
            });
            if (response.ok) {
                alert("Client eliminat correctament!");
                fetchClients();
            } else {
                alert("Error al eliminar el client.");
            }
        } catch (error) {
            alert(`Error de connexió: ${error.message}`);
        }
    }
}

document.addEventListener("DOMContentLoaded", fetchClients);