#!/usr/bin/node

const argvC = process.argv.length;
const argvP = Math.trunc(process.argv[2]);
let i = 0;
if (argvC < 3 || !Number(argvP)) console.log('Missing number of occurrences');
else {
  if (argvP >= 0) {
    while (i < argvP) {
      console.log('C is fun');
      i++;
    }
  }
}
