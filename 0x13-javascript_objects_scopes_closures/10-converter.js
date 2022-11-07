#!/usr/bin/node
// function that converts a number from base 10 to another base passed as argument: return converter
exports.converter = function (base) {
	function converter (num) {
		return num.toString(base);
	};
	return converter
};
