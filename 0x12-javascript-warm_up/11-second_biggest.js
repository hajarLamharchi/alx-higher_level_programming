#!/usr/bin/node
const arg = process.argv;
if (arg.length <= 3) {
  console.log(0);
} else {
  arg.sort();
  console.log(arg[arg.length - 2]);
}
