3!/usr/bin/node
//script that searches the second biggest integer in the list of arguments.
if (process.argv.length <= 2) {
	console.log(0);
} else {
	const list = process.argv.sort();
	console.log(list.reverse()[1]);
}
