document.addEventListener('DOMContentLoaded', () => {
    // Seleccionem el mòdul d'usuaris
    const usersModule = document.getElementById('usersModule');

    // Afegim event listener per al clic
    usersModule.addEventListener('click', () => {
        // Redireccionem a la pàgina del formulari
        window.location.href = '/ususaris/index_form.html';
    });

    // Opcional: Afegir efecte al passar el ratolí
    usersModule.addEventListener('mouseenter', () => {
        usersModule.style.borderColor = '#714B67';
    });

    usersModule.addEventListener('mouseleave', () => {
        usersModule.style.borderColor = '#e0e0e0';
    });

     // Mòdul Punt de venda
    const puntModule = document.getElementById('productsModule');

    puntModule.addEventListener('click', () => {
        window.location.href = '/productes/index_form.html';
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