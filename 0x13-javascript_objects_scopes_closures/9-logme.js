#!/usr/bin/node
exports.logMe = function (item) {
  if (this.t === undefined) {
    this.t = 0;
  }
  console.log(this.t + ': ' + item);
  this.t++;
};
