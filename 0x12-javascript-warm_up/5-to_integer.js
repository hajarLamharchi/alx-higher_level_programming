#!/usr/bin/node
if (Number.isInteger(process.argv[2])) {
  console.log('My number: ' + process.argv[2]);
} else if (Number.isInteger(parseInt(process.argv[2]))) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
