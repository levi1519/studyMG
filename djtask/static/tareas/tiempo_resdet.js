// Obtener todos los elementos con la clase "tiempo-restante"
var elementosTiempoRestante = document.querySelectorAll('.tiempo-restante');

// Iterar sobre cada elemento
elementosTiempoRestante.forEach(function(elementoTiempoRestante) {
    // Obtener la fecha límite y la hora límite de los atributos de datos
    var fechaLimiteCompleta = new Date(elementoTiempoRestante.getAttribute('data-fechalimite') + ' ' + elementoTiempoRestante.getAttribute('data-horalimite'));

    // Obtener la fecha y hora actuales
    var fechaActual = new Date();

    // Calcular el tiempo restante en milisegundos
    var tiempoRestanteMs = fechaLimiteCompleta - fechaActual;

    // Verificar si la fecha límite es en el futuro
    if (tiempoRestanteMs > 0) {
        // Calcular los días, horas y minutos restantes
        var diasRestantes = Math.floor(tiempoRestanteMs / (1000 * 60 * 60 * 24));
        var horasRestantes = Math.floor((tiempoRestanteMs % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutosRestantes = Math.floor((tiempoRestanteMs % (1000 * 60 * 60)) / (1000 * 60));

        // Construir el texto del tiempo restante
        var textoTiempoRestante = '';
        if (diasRestantes > 0) {
            textoTiempoRestante += diasRestantes + ' días, ';
        }
        textoTiempoRestante += horasRestantes + ' horas y ' + minutosRestantes + ' minutos';

        // Actualizar el texto del tiempo restante en este elemento
        elementoTiempoRestante.textContent = textoTiempoRestante;
    } else {
        // Si la fecha límite ha pasado, mostrar "Expirado"
        elementoTiempoRestante.textContent = 'Expirado';
    }
});
