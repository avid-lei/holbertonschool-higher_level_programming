#!/usr/bin/node

function factorial (n) {
  if (n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}
const n = process.argv[2];
if (!n) {
  console.log(1);
} else {
  console.log(factorial(n));
}
