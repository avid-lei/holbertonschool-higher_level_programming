#!/usr/bin/node

function check (s) {
  if (s) {
    return (s);
  } else {
    return ('undefined');
  }
}

console.log(check(process.argv[2]), 'is', check(process.argv[3]));
