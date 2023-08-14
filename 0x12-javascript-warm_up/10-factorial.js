#!/usr/bin/node
const x = parseInt(process.argv[2]);

console.log(fac(x));

function fac (a) {
  if (isNaN(a)) {
    return (1);
  }
  if (a === 1) {
    return (1);
  }
  return (a * fac(a - 1));
}
