const API_URL = "http://localhost:8000/empleados";

async function fetchEmpleados() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const empleados = await response.json();
        displayEmpleados(empleados);
    } catch (error) {
        console.error("Error al obtenir els empleats:", error);
    }
}

function displayEmpleados(empleados) {
    const tableBody = document.querySelector("#empleadosTable tbody");
    tableBody.innerHTML = "";

    empleados.forEach(data => {
        const empleado = data.empleado;
        const row = document.createElement("tr");

        const idCell = document.createElement("td");
        idCell.textContent = empleado.ID_empleado;
        row.appendChild(idCell);

        const nameCell = document.createElement("td");
        nameCell.textContent = empleado.nombre;
        row.appendChild(nameCell);

        const cargoCell = document.createElement("td");
        cargoCell.textContent = empleado.cargo;
        row.appendChild(cargoCell);

        const ssCell = document.createElement("td");
        ssCell.textContent = empleado.ss;
        row.appendChild(ssCell);

        const sueldoCell = document.createElement("td");
        sueldoCell.textContent = empleado.sueldo;
        row.appendChild(sueldoCell);

        const actionsCell = document.createElement("td");
        actionsCell.innerHTML = `
            <button onclick="editEmpleado(${empleado.ID_empleado})">Editar</button>
            <button onclick="deleteEmpleado(${empleado.ID_empleado})">Eliminar</button>
        `;
        row.appendChild(actionsCell);

        tableBody.appendChild(row);
    });
}

function editEmpleado(id) {
    window.location.href = `index_form_empleados.html?id=${id}`;
}

async function deleteEmpleado(id) {
    if (confirm("Estàs segur d'eliminar aquest empleat?")) {
        try {
            const response = await fetch(`http://localhost:8000/empleado/delete/${id}`, {
                method: 'DELETE'
            });
            if (response.ok) {
                alert("Empleat eliminat correctament!");
                fetchEmpleados();
            } else {
                alert("Error al eliminar l'empleat.");
            }
        } catch (error) {
            alert(`Error de connexió: ${error.message}`);
        }
    }
}

document.addEventListener("DOMContentLoaded", fetchEmpleados);