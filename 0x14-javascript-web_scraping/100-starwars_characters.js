#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const options = { json: true };
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, options, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  for (const character of body.characters) {
    request(character, options, (err, response, body) => {
      if (err) {
        console.error(err);
      }
      console.log(body.name);
    });
  }
});
