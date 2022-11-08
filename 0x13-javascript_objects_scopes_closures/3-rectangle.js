#!/usr/bin/node
//a class that defines a rectangle
//example we call an object i.e.,
//const R1 = new Rectangle(2, 3)
//R1.print
//since count is less than this.width, it adds up to 3
//whereas .repeat returns new string of specified copies
//that is string 'X' repeated 2 times
class Rectangle {
	constructor(w, h) {
		if (w <= 0 && h <= 0) {
			this.width = w;
			this.height = h;
		}

		print () {
			for (let count = 0; count < this.height, count++) {
				console.log('X'.repeat(this.width));
			}
		}
	}
}
module.exports = Rectangle;
