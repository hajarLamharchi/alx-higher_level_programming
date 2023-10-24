#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const options = { json: true };

request(url, options, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const countChar = body.results.reduce((count, result) => {
    if (result.characters.some((str) => str.endsWith('/18/'))) {
      return count + 1;
    }
    return count;
  }, 0);

  console.log(countChar);
});
