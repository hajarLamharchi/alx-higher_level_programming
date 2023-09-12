#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.isValid = false;
    } else {
      this.width = w;
      this.height = h;
      this.isValid = true;
    }
  }
}
module.exports = Rectangle;
