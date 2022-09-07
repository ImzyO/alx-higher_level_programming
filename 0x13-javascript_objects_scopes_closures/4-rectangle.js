#!/usr/bin/node
//class Rectangle defines a Rectangle
class Rectangle {
	constructor(w, h) {
		if (w <= 0 && h <= 0) {
			this.width = w;
			this.height = h;
		}
	}
	print() {
		for (let count = 0; count < this.height; count++) {
			console.log('X'.repeat(this.width));
		}
	}
	rotate() {
		let exchange = this.width;
		this.width = this.height;
		this.height = exchange;
	}
	double() {
		this.width = this.width * 2;
		this.height = this.height * 2;
	}
}
module.exports = Rectangle;
