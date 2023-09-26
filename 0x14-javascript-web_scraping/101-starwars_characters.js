#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(`${url}${args[0]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      const data = JSON.parse(body).characters;
      printCharacters(data, 0);
    }
  }
});

function printCharacters (data, index) {
  request(data[index], (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      if (response.statusCode === 200) {
        const name = JSON.parse(body).name;
        console.log(name);
      }
    }
  });

  if (index < data.length - 1) { printCharacters(data, index + 1); }
}
