#!/usr/bin/node
let x = process.argv[2];
if (!parseInt(x)) {
  console.log('Missing size');
}
if (x > 0) {
  const s = 'X'.repeat(x);

  while (x > 0) {
    console.log(s);
    x--;
  }
}
