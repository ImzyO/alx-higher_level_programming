#!/usr/bin/node
// a class that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

<<<<<<< HEAD
		print () {
			for (let count = 0; count < this.height, count++) {
				console.log('X'.repeat(this.width));
			}
		}
	}
=======
  print () {
    console.log(('X'.repeat(this.width) + '\n').repeat(this.height - 1) + 'X'.repeat(this.width));
  }
>>>>>>> f1821400090ecada8e3ed35bfe676aebd8f9f449
}
module.exports = Rectangle;
