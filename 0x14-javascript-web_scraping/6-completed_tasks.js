#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const options = { json: true };

const dict = {};
request(url, options, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  body.forEach((task) => {
    if (task.completed) {
      const id = task.userId;
      if (dict[id] === undefined) {
        dict[id] = 1;
      } else {
        dict[id]++;
      }
    }
  });
  console.log(dict);
});
