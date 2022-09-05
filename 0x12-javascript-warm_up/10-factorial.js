#!/usr/bin/node
//script that computes and prints a factorial
function factorial (i) {
	if ((isNaN(i)) || (i === 1)) {
		return 1;
	} else {
		return i * factorial(i - 1);
	}
}
console.log(factorial(parseInt(process.argv[2])));
