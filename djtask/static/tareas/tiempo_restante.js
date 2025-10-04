
/*
//lista
 
document.addEventListener('DOMContentLoaded', function() {
  // Obtener todos los elementos con la clase "actividad"
  var actividades = document.querySelectorAll('.actividad');

  // Iterar sobre cada elemento
  actividades.forEach(function(actividad) {
      // Obtener la fecha límite y la hora límite de los atributos de datos
      var fechaLimite = new Date(actividad.getAttribute('data-fechalimite') + ' ' + actividad.getAttribute('data-horalimite'));

      // Obtener la fecha y hora actuales
      var fechaActual = new Date();

      // Calcular el tiempo restante en milisegundos
      var tiempoRestanteMs = fechaLimite - fechaActual;

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

          // Actualizar el texto del tiempo restante
          actividad.querySelector('.tiempo-restante').textContent = textoTiempoRestante;
      } else {
          // Si la fecha límite ha pasado, mostrar "Expirado"
          actividad.querySelector('.tiempo-restante').textContent = 'Expirado';
      }
  });
});

*/

function calcularTiempoRestante(actividad) {
  var fechaLimite = new Date(actividad.getAttribute('data-fechalimite') + ' ' + actividad.getAttribute('data-horalimite'));
  var fechaActual = new Date();
  var tiempoRestanteMs = fechaLimite - fechaActual;

  if (tiempoRestanteMs > 0) {
      var diasRestantes = Math.floor(tiempoRestanteMs / (1000 * 60 * 60 * 24));
      var horasRestantes = Math.floor((tiempoRestanteMs % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutosRestantes = Math.floor((tiempoRestanteMs % (1000 * 60 * 60)) / (1000 * 60));

      var textoTiempoRestante = '';
      if (diasRestantes > 0) {
          textoTiempoRestante += diasRestantes + ' días, ';
      }
      textoTiempoRestante += horasRestantes + ' horas y ' + minutosRestantes + ' minutos';
      actividad.querySelector('.tiempo-restante').textContent = textoTiempoRestante;
  } else {
      actividad.querySelector('.tiempo-restante').textContent = 'Expirado';
  }
}

function inicializarTiempoRestante() {
  var actividades = document.querySelectorAll('.actividad');
  actividades.forEach(function(actividad) {
      calcularTiempoRestante(actividad);
  });
}

// Llamar inicializarTiempoRestante en la pagina de detalles si solo hay un elemento 


document.addEventListener('DOMContentLoaded', function() {
  // Si estás en la página de detalles de la actividad, y solo hay un elemento para calcular el tiempo restante
  var actividadDetalle = document.querySelector('.actividad');
  if (actividadDetalle) {
      calcularTiempoRestante(actividadDetalle);
  }
});


/*
document.addEventListener('DOMContentLoaded', function() {
  // Obtener el elemento que mostrará el tiempo restante
  var elementoTiempoRestante = document.querySelector('#tiempo-restante');

  // Obtener el tiempo restante desde el atributo de datos del elemento
  var diasRestantes = parseInt(elementoTiempoRestante.getAttribute('data-dias'));
  var horasRestantes = parseInt(elementoTiempoRestante.getAttribute('data-horas'));
  var minutosRestantes = parseInt(elementoTiempoRestante.getAttribute('data-minutos'));

  // Construir el texto del tiempo restante
  var textoTiempoRestante = '';
  if (diasRestantes > 0) {
    textoTiempoRestante += diasRestantes + ' días, ';
  }
  textoTiempoRestante += horasRestantes + ' horas y ' + minutosRestantes + ' minutos';

  // Actualizar el texto del tiempo restante en el elemento correspondiente
  elementoTiempoRestante.textContent = textoTiempoRestante;
});

*/





// lista y detalle 2:

// Función para calcular el tiempo restante
function calcularTiempoRestante(fechaLimite, horaLimite, elementoTiempoRestante) {
  // Obtener la fecha y hora actuales
  var fechaActual = new Date();

  // Obtener la fecha límite y la hora límite como objetos Date
  var fechaLimiteCompleta = new Date(fechaLimite + ' ' + horaLimite);

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

      // Actualizar el texto del tiempo restante en el elemento correspondiente
      elementoTiempoRestante.textContent = textoTiempoRestante;
  } else {
      // Si la fecha límite ha pasado, mostrar "Expirado"
      elementoTiempoRestante.textContent = 'Expirado';
  }
}

document.addEventListener('DOMContentLoaded', function() {
  // Obtener todos los elementos con la clase "actividad"
  var actividades = document.querySelectorAll('.actividad');

  // Iterar sobre cada elemento
  actividades.forEach(function(actividad) {
      // Obtener los atributos de datos de la actividad
      var fechaLimite = actividad.getAttribute('data-fechalimite');
      var horaLimite = actividad.getAttribute('data-horalimite');
      var elementoTiempoRestante = actividad.querySelector('.tiempo-restante');

      // Calcular y mostrar el tiempo restante
      calcularTiempoRestante(fechaLimite, horaLimite, elementoTiempoRestante);
  });

  // Obtener el elemento del tiempo restante en la página de detalle
  var tiempoRestanteDetalle = document.querySelector('#tiempo-restante-detalle');

  if (tiempoRestanteDetalle) {
      // Obtener los atributos de datos en la página de detalle
      var fechaLimiteDetalle = tiempoRestanteDetalle.getAttribute('data-fechalimite');
      var horaLimiteDetalle = tiempoRestanteDetalle.getAttribute('data-horalimite');

      // Calcular y mostrar el tiempo restante en la página de detalle
      calcularTiempoRestante(fechaLimiteDetalle, horaLimiteDetalle, tiempoRestanteDetalle);
  }
});


 /*
/*
// detalle 3
// Función para calcular el tiempo restante
function calcularTiempoRestante(fechaLimite, horaLimite, elementoTiempoRestante) {
    // Obtener la fecha y hora actual en formato ISO
    var fechaHoraActual = new Date().toISOString().slice(0, 16);
  
    // Concatenar la fecha límite y hora límite para formar una cadena de fecha completa
    var fechaHoraLimite = fechaLimite + 'T' + horaLimite;
  
    // Crear objetos Date para la fecha y hora límite
    var fechaLimiteCompleta = new Date(fechaHoraLimite);
    var fechaActual = new Date(fechaHoraActual);
  
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
  
      // Actualizar el texto del tiempo restante en el elemento correspondiente
      elementoTiempoRestante.textContent = textoTiempoRestante;
    } else {
      // Si la fecha límite ha pasado, mostrar "Expirado"
      elementoTiempoRestante.textContent = 'Expirado';
    }
  }
  
  document.addEventListener('DOMContentLoaded', function() {
    // Obtener el elemento del tiempo restante en la página de detalle
    var tiempoRestanteDetalle = document.querySelector('#tiempo-restante');
  
    if (tiempoRestanteDetalle) {
      // Obtener los atributos de datos en la página de detalle
      var fechaLimiteDetalle = tiempoRestanteDetalle.getAttribute('data-fechalimite');
      var horaLimiteDetalle = tiempoRestanteDetalle.getAttribute('data-horalimite');
  
      // Calcular y mostrar el tiempo restante en la página de detalle
      calcularTiempoRestante(fechaLimiteDetalle, horaLimiteDetalle, tiempoRestanteDetalle);
    }
  });
  */

  // Función para calcular el tiempo restante
function calcularTiempoRestante(fechaLimite, horaLimite, elementoTiempoRestante) {
    // Obtener la fecha y hora actuales
    var fechaActual = new Date();
  
    // Obtener la fecha límite y la hora límite como objetos Date
    var fechaLimiteCompleta = new Date(fechaLimite + ' ' + horaLimite);
  
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
  
        // Actualizar el texto del tiempo restante en el elemento correspondiente
        elementoTiempoRestante.textContent = textoTiempoRestante;
    } else {
        // Si la fecha límite ha pasado, mostrar "Expirado"
        elementoTiempoRestante.textContent = 'Expirado';
    }
  }
  
  document.addEventListener('DOMContentLoaded', function() {
    // Obtener el elemento del tiempo restante en la página de detalle
    var tiempoRestanteDetalle = document.querySelector('#tiempo-restante');
  
    if (tiempoRestanteDetalle) {
        // Obtener los atributos de datos en la página de detalle
        var fechaLimite = tiempoRestanteDetalle.getAttribute('data-fechalimite');
        var horaLimite = tiempoRestanteDetalle.getAttribute('data-horalimite');
  
        // Calcular y mostrar el tiempo restante en la página de detalle
        calcularTiempoRestante(fechaLimite, horaLimite, tiempoRestanteDetalle);
    }
  });
  