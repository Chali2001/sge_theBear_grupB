const API_URL = "http://localhost:8000/empleados";

async function fetchEmpleats() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const empleats = await response.json();
        displayEmpleats(empleats);
    } catch (error) {
        console.error("Error al obtenir els empleats:", error);
    }
}

function displayEmpleats(empleats) {
    const tableBody = document.querySelector("#empleatsTable tbody");
    tableBody.innerHTML = "";

    empleats.forEach(data => {
        const empleat = data.empleado;
        const row = document.createElement("tr");

        const idCell = document.createElement("td");
        idCell.textContent = empleat.ID_empleado;
        row.appendChild(idCell);

        const nameCell = document.createElement("td");
        nameCell.textContent = empleat.nombre;
        row.appendChild(nameCell);

        const carrecCell = document.createElement("td");
        carrecCell.textContent = empleat.cargo;
        row.appendChild(carrecCell);

        const ssCell = document.createElement("td");
        ssCell.textContent = empleat.ss;
        row.appendChild(ssCell);

        const souCell = document.createElement("td");
        souCell.textContent = empleat.sueldo;
        row.appendChild(souCell);

        const actionsCell = document.createElement("td");
        actionsCell.innerHTML = `
            <button aria-label="Editar empleat ${empleat.nombre}" onclick="editEmpleat(${empleat.ID_empleado})">Editar</button>
            <button aria-label="Eliminar empleat ${empleat.nombre}" onclick="deleteEmpleat(${empleat.ID_empleado})">Eliminar</button>
        `;
        row.appendChild(actionsCell);

        tableBody.appendChild(row);
    });
}

function editEmpleat(id) {
    window.location.href = `index_form_empleats.html?id=${id}`;
}

async function deleteEmpleat(id) {
    if (confirm("Estàs segur d'eliminar aquest empleat?")) {
        try {
            const response = await fetch(`http://localhost:8000/empleado/delete/${id}`, {
                method: 'DELETE'
            });
            if (response.ok) {
                alert("Empleat eliminat correctament!");
                fetchEmpleats();
            } else {
                alert("Error al eliminar l'empleat.");
            }
        } catch (error) {
            alert(`Error de connexió: ${error.message}`);
        }
    }
}

document.addEventListener("DOMContentLoaded", fetchEmpleats);