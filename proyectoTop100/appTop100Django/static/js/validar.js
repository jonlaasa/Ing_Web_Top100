function validarForm() {
    // Obtener el elemento select
    var select = document.getElementById('canciones');
    
    // Comprobar si se ha seleccionado al menos una opción
    if (select.selectedOptions.length === 0) {
        // Si no se ha seleccionado ninguna opción, mostrar un mensaje
        alert("Por favor, selecciona al menos una canción para votar.");
        return false;  // Evitar el envío del formulario
    }
    
    // Si se seleccionó al menos una opción, permitir el envío del formulario
    return true;
}

function borrarWarn() {
    // Esta función la puedes utilizar para eliminar cualquier mensaje anterior si es necesario
    // No la necesitamos en este caso, pero la dejamos por si en el futuro quieres expandir la funcionalidad
}