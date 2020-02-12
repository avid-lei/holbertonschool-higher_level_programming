#!/usr/bin/node
request = require("request")
fs = require("fs")
url = process.argv[2]
file = process.argv[3]
request(url, function(err, repsonse, body){
    fs.writeFile(file, body, 'utf-8', function(err) {
        if (err)
            console.log(err);
    });
});