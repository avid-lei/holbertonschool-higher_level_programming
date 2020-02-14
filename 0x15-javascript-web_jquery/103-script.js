#!/usr/bin/node
$(document).ready(function () {

    let translate = function(){
        $.ajax({
          url: 'https://www.fourtonfish.com/hellosalut/',
          type: 'get',
          data: { lang: $('INPUT#language_code').val() },
          success: function (result) {
            $('DIV#hello').html(result.hello);
          }
        });
      }


    $('INPUT#btn_translate').click(translate());
  });
