#!/usr/bin/node

const argvC = process.argv.length;
const argvP = process.argv[2];

if (argvC < 3) console.log('No argument');
else console.log(argvP);
