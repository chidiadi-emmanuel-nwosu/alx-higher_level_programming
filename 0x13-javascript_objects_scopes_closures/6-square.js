#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let x = '';
      for (let i = 0; i < this.width; i++) {
        x += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(x);
      }
    }
  }
}

module.exports = Square;
