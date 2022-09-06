#!/usr/bin/node

const fargv = Number(process.argv[2]);
const sargv = Number(process.argv[3]);

add(fargv, sargv);
function add (a, b) {
  console.log(a + b);
}
