#!/usr/bin/node
//function that returns the reversed version of a list
exports.esrever = function (list) {
	let resvlist = [];
	for (let index = list.length - 1; index >= 0; index--) {
		resvlist.push(list[index]);
	}
	return resvlist;
};
