const API

_URL = "http://localhost:8000/clientes";

async function fetchClientes() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const clientes = await response.json();
        displayClientes(clientes);
    } catch (error) {
        console.error("Error al obtenir els clients:", error);
    }
}

function displayClientes(clientes) {
    const tableBody = document.querySelector("#clientesTable tbody");
    tableBody.innerHTML = "";

    clientes.forEach(data => {
        const cliente = data.cliente;
        const row = document.createElement("tr");

        const idCell = document.createElement("td");
        idCell.textContent = cliente.ID_cliente;
        row.appendChild(idCell);

        const nameCell = document.createElement("td");
        nameCell.textContent = cliente.nombre;
        row.appendChild(nameCell);

        const telefonoCell = document.createElement("td");
        telefonoCell.textContent = cliente.telefono;
        row.appendChild(telefonoCell);

        const actionsCell = document.createElement("td");
        actionsCell.innerHTML = `
            <button onclick="editCliente(${cliente.ID_cliente})">Editar</button>
            <button onclick="deleteCliente(${cliente.ID_cliente})">Eliminar</button>
        `;
        row.appendChild(actionsCell);

        tableBody.appendChild(row);
    });
}

function editCliente(id) {
    window.location.href = `index_form_clientes.html?id=${id}`;
}

async function deleteCliente(id) {
    if (confirm("Estàs segur d'eliminar aquest client?")) {
        try {
            const response = await fetch(`http://localhost:8000/cliente/delete/${id}`, {
                method: 'DELETE'
            });
            if (response.ok) {
                alert("Client eliminat correctament!");
                fetchClientes();
            } else {
                alert("Error al eliminar el client.");
            }
        } catch (error) {
            alert(`Error de connexió: ${error.message}`);
        }
    }
}

document.addEventListener("DOMContentLoaded", fetchClientes);