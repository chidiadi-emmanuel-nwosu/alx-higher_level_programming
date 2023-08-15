#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    for (let i = 0; i < this.width; i++) {
      x += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(x);
    }
  }
}

module.exports = Rectangle;
