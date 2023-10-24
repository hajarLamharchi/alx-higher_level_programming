#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const endPoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
const options = { json: true };

request(endPoint, options, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  console.log(body.title);
});
