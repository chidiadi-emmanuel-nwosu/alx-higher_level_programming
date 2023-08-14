#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let y = '';
  for (let i = 0; i < x; i++) {
    y = y + 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(y);
  }
}
