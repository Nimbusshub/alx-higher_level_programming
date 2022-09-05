#!/usr/bin/node

const argvP = Math.trunc(process.argv[2]);

if (Number(argvP)) console.log('My number: ' + argvP);
else console.log('Not a number');
