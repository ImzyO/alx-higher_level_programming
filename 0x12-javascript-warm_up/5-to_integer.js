#!/usr/bin/node
//a script that prints a string if the first argument can be converted to int
if (isNaN(process.argv[2])) {
	console.log('Not a number');
} else {
	console.log('My number: ' + parseInt(process.argv[2]));
