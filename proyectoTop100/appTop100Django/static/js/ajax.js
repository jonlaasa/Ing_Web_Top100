$(document).ready(function() {

  $('section.topcanciones a').each(function () {
    var href = $(this).attr("href");
    href = href.replace("canciones", "cancionAjax");
    $(this).qtip({
       content: {
          url: href,
          method: 'get'
       }
    });
  });

});