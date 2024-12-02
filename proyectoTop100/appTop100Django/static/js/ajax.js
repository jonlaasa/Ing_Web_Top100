$(document).ready(function() {

  var csrf_token = $('meta[name="csrf-token"]').attr('content');

  $('section.topcanciones a').each(function () {
    var href = $(this).attr("href");
    href = href.replace("canciones", "cancionAjax");
    
    $(this).qtip({
      content: {
         url: href,
         method: 'get',
         ajax: {
           beforeSend: function(xhr) {
             // Agregar el token CSRF a las cabeceras de la solicitud
             xhr.setRequestHeader("X-CSRFToken", csrf_token);
           }
         }
      }
    });
  });

});