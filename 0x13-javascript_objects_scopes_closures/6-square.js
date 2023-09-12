#!/usr/bin/node

const SquareOne = require('./5-square');

class Square extends SquareOne {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += c;
      }

      for (let j = 0; j < this.height; j++) {
        console.log(row);
      }
    }
  }
}

module.exports = Square;
