#!/usr/bin/node

const SquareSC = require('./5-square');

class Square extends SquareSC {
  charPrint (c) {
    if (c) {
      for (let j = 0; j < this.height; j++) {
        const temp = [];
        for (let i = 0; i < this.height; i++) temp.push(c);
        console.log(temp.join(''));
      }
    } else super.print();
  }
}

module.exports = Square;
