#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const options = { json: true };

let c = 0;

request(url, options, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const results = body.results;
  for (let i = 0; i < body.count; i++) {
    if (results[i].characters.some((str) => str.endsWith('/18/'))) {
      c += 1;
    }
  }
  console.log(c);
});
