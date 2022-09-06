#!/usr/bin/node

const argvP = Math.trunc(process.argv[2]);
let i = 0;
if (!Number(argvP)) console.log("Missing size");
else {
  if (argvP >= 1) {
    while (i < Number(argvP)) {
      const cont = [];
      for (let j = 0; j < Number(argvP); j++) {
        cont.push("X");
      }
      console.log(cont.join(""));
      i++;
    }
  }
}
