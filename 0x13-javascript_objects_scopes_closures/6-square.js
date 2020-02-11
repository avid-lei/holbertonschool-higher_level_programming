#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c = 'X') {
    const s = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(s);
    }
  }
};
