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
});