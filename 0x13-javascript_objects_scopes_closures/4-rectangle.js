#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // prints the rectangle with 'X'
  print () {
    for (let j = 0; j < this.height; j++) {
      const temp = [];
      for (let i = 0; i < this.width; i++) temp.push('X');
      console.log(temp.join(''));
    }
  }

  // rotates and exchanges the width and the height of the rectangle.
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // doubles and mutiply the width and the height of the rectangle by 2.
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
