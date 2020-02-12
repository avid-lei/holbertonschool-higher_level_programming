#!/usr/bin/node
request = require("request")
request("https://swapi.co/api/people/18/", function(err, response, body){
    info = JSON.parse(body)
    console.log(info.films.length)
});