document.addEventListener('DOMContentLoaded', () => {
    // Mòdul Punt de Venda
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

    // Mòdul Factura
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

    // Mòdul Clients
    const clientsModule = document.getElementById('clientsModule');
    clientsModule.addEventListener('click', () => {
        window.location.href = 'Clientes/clientes.html';
    });
    clientsModule.addEventListener('mouseenter', () => {
        clientsModule.style.borderColor = '#714B67';
    });
    clientsModule.addEventListener('mouseleave', () => {
        clientsModule.style.borderColor = '#e0e0e0';
    });

    // Mòdul Empleats
    const empleatsModule = document.getElementById('empleatsModule');
    empleatsModule.addEventListener('click', () => {
        window.location.href = 'Empleados/empleados.html';
    });
    empleatsModule.addEventListener('mouseenter', () => {
        empleatsModule.style.borderColor = '#714B67';
    });
    empleatsModule.addEventListener('mouseleave', () => {
        empleatsModule.style.borderColor = '#e0e0e0';
    });
});