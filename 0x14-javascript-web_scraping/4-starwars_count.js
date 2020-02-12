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
    while (i < info.length) {
      let j = 0;
      while (j < info[i].characters.length) {
        if (info[i].characters[j].includes('/18/')) {
          count++;
        }
        j++;
      }
      i++;
    }
    console.log(count);
  }
});
