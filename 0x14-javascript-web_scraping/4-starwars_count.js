#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    let info = JSON.parse(body);
    info = info.results;
    let i = 0;
    let count = 0;
    while (info[i]) {
      if (info[i].characters.indexOf('https://swapi.co/api/people/18/') > -1) {
        count++;
      }
      i++;
    }
    console.log(count);
  }
});
