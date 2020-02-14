#!/usr/bin/node
$.ajax({
  url: 'https://swapi.co/api/people/5/?format=json',
  success: function (result) {
    $('#character').html(result.name);
  }
});
