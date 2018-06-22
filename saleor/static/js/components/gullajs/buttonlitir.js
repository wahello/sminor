$(document).ready(function() {

  // sækjum takkana
  const $takkar = $(".variant-picker").children(".btn-group").children();

  // ef það eru takkar
  if ($takkar.length > 0) {

    $takkar.each(function() {

      var e = $(this);
      var litur = e.text();
////////////////////////////////////////////////////////////////
    /*  if (litur == 'Gulur') {
        e.attr("style", "background: yellow;");
      }
      else if (litur == 'Rauður') {
        e.attr("style", "background: red;")
      }*/
//////////////////////////////////////////////////////////////
    });

  }

});
