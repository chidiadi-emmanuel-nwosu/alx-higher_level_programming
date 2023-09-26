#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;
let characters = [];

request(url, (err, response, body) => {
  if (!err) {
      const data = JSON.parse(body)
      characters = data.characters;
      printCharacters(characters, 0);
  }
});

function printCharacters (data, index) {
  request(data[index], (err, response, body) => {
    if (!err) {
        const name = JSON.parse(body).name;
        console.log(name);
    }
  });

  if (index < data.length - 1) { printCharacters(data, index + 1); }
}
