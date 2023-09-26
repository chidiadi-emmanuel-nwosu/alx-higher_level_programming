#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      console.log(data.title);
    }
  }
});
