#!/usr/bin/node
let fs = require("fs")
let file = process.argv[2]

fs.readFile(file, function(err, data) {
    if (err) {
        console.error(err);
    } else {
        console.log(data.toString());
    }
});