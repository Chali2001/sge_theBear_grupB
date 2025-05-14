document.addEventListener('DOMContentLoaded', () => {
    const puntModule = document.getElementById('puntModule');
    puntModule.addEventListener('click', () => {
        window.location.href = 'Punt_de_venda/index_form.html';
    });
    puntModule.addEventListener('mouseenter', () => {
        puntModule.style.borderColor = '#714B67';
    });
    puntModule.addEventListener('mouseleave', () => {
        puntModule.style.borderColor = '#e0e0e0';
    });

    const facturaModule = document.getElementById('facturaModule');
    facturaModule.addEventListener('click', () => {
        window.location.href = 'Factura/index_form.html';
    });
    facturaModule.addEventListener('mouseenter', () => {
        facturaModule.style.borderColor = '#714B67';
    });
    facturaModule.addEventListener('mouseleave', () => {
        facturaModule.style.borderColor = '#e0e0e0';
    });

    const clientesModule = document.getElementById('clientesModule');
    clientesModule.addEventListener('click', () => {
        window.location.href = 'Clientes/index_table.html';
    });
    clientesModule.addEventListener('mouseenter', () => {
        clientesModule.style.borderColor = '#714B67';
    });
    clientesModule.addEventListener('mouseleave', () => {
        clientesModule.style.borderColor = '#e0e0e0';
    });

    const empleadosModule = document.getElementById('empleadosModule');
    empleadosModule.addEventListener('click', () => {
        window.location.href = 'Empleados/index_table.html';
    });
    empleadosModule.addEventListener('mouseenter', () => {
        empleadosModule.style.borderColor = '#714B67';
    });
    empleadosModule.addEventListener('mouseleave', () => {
        empleadosModule.style.borderColor = '#e0e0e0';
    });
});