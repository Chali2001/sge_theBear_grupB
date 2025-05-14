document.addEventListener('DOMContentLoaded', () => {
    // Seleccionem els mòduls
    const usersModule = document.getElementById('usersModule');
    const empleatsModule = document.getElementById('empleatsModule');
    const clientsModule = document.getElementById('clientsModule');

    // Event listener per al mòdul d'ususariss
    usersModule.addEventListener('click', () => {
        window.location.href = './ususaris/index_form.html';
    });
    usersModule.addEventListener('mouseenter', () => {
        usersModule.style.borderColor = '#714B67';
    });
    usersModule.addEventListener('mouseleave', () => {
        usersModule.style.borderColor = '#e0e0e0';
    });

    // Event listener per al mòdul d'empleats
    empleatsModule.addEventListener('click', () => {
        window.location.href = './ususaris/index_form_empleats.html';
    });
    empleatsModule.addEventListener('mouseenter', () => {
        empleatsModule.style.borderColor = '#714B67';
    });
    empleatsModule.addEventListener('mouseleave', () => {
        empleatsModule.style.borderColor = '#e0e0e0';
    });

    // Event listener per al mòdul de clients
    clientsModule.addEventListener('click', () => {
        window.location.href = './ususaris/index_form_clients.html';
    });
    clientsModule.addEventListener('mouseenter', () => {
        clientsModule.style.borderColor = '#714B67';
    });
    clientsModule.addEventListener('mouseleave', () => {
        clientsModule.style.borderColor = '#e0e0e0';
    });
});