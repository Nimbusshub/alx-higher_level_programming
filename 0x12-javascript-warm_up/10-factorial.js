#!/usr/bin/node

const fargv = Number(process.argv[2]);

function factorialF (valueF) {
  if (valueF < 0) return;
  if (valueF === 0 || isNaN(valueF)) return 1;
  return valueF * factorialF(valueF - 1);
}
console.log(factorialF(fargv));
