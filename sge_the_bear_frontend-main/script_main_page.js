document.addEventListener('DOMContentLoaded', () => {
    // Seleccionem el mòdul d'usuaris
    const facturaModule = document.getElementById('facturaModule');

    // Afegim event listener per al clic
    facturaModule.addEventListener('click', () => {
        // Redireccionem a la pàgina del formulari
        window.location.href = 'Factura/index_form.html';
    });

    // Opcional: Afegir efecte al passar el ratolí
    facturaModule.addEventListener('mouseenter', () => {
        facturaModule.style.borderColor = '#714B67';
    });

    facturaModule.addEventListener('mouseleave', () => {
        facturaModule.style.borderColor = '#e0e0e0';
    });

     // Mòdul Punt de venda
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

    // Modul Factura
    const invoiceModule = document.getElementById('invoiceModule');
    
    invoiceModule.addEventListener('click', () => {
        window.location.href = '/factura/index_form.html';
    });
    invoiceModule.addEventListener('mouseenter', () => {
        invoiceModule.style.borderColor = '#714B67';
    });
    invoiceModule.addEventListener('mouseleave', () => {
        invoiceModule.style.borderColor = '#e0e0e0';
    });
});