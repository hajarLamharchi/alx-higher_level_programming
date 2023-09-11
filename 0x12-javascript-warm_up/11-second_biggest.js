#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[2] === null) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  let max = process.argv[2];
  let secondMax = 0;
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      secondMax = max;
      max = process.argv[i];
    } else if (process.argv[i] > secondMax && process.argv[i] <= max) {
      secondMax = process.argv[i];
    }
  }
  if (secondMax === 0) {
    console.log(0);
  } else {
    console.log(secondMax);
  }
}
