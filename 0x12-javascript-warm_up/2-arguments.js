#!/usr/bin/node
// import {argv} from `node:process`;

const argvC = process.argv.length;

if (argvC < 3) {
  console.log('No argument');
} else if (argvC === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
