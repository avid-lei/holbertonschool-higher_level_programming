#!/usr/bin/node
let x = process.argv[2];
if (!parseInt(x)) {
  console.log('Missing number of occurrences');
}

while (x > 0) {
  console.log('C is fun');
  x--;
}
