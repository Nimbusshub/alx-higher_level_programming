#!/usr/bin/node

const argvC = process.argv.length;
const array = [];

if (argvC < 4) console.log(0);
else {
  for (let i = 2; i < argvC; i++) array.push(Number(process.argv[i]));

  const count = argvC - 2;
  for (const x in array) {
    const k = Number(x);
    let j = k;
    while (j < count) {
      if (array[k] > array[j]) {
        const temp = array[k];
        array[k] = array[j];
        array[j] = temp;
      }
      j++;
    }
  }
  console.log(array[count - 2]);
}
