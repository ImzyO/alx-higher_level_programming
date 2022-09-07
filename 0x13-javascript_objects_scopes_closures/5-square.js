#!/usr/bin/node
//class Square defines square and inherits from Rectangle of 4-rectangle.js
//super () method calls parent's constructor method,
//and gets access to parent's properties and methods
class Square {
	constructor(size) {
		super(w, h);
		this.size = size;
	}
}
module.exports = Square;
