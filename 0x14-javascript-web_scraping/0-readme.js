#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data.toString());
  }
});
