#!/usr/bin/node
//class Square Defines a square inherits from Square of 5-square.js:
class Square extends Square {
	super(name, size);

	charPrint(c) {
		if (c) {
			for (let count = 0; count < this.height; count++) {
				console.log('c'.repeat(this.width));
			}
		} else if (c === undefined) {
			for (count2 = 0; count2 < this.height; count2++) {
				console.log('X'.repeat(this.width));
			}
		}
	}
}
module.exports = Square;
