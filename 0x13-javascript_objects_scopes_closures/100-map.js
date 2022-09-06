#!/usr/bin/node

const Array1 = require("./100-data").list;
const Array2 = Array1.map((element, index) => element * index);
console.log(Array1);
console.log(Array2);
