#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;
let characters = [];

request(url, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    characters = data.characters;
    printCharacters(0);
  }
});

function printCharacters (index) {
  if (index === characters.length) { return; }
  request(characters[index], (err, response, body) => {
    if (!err) {
      const name = JSON.parse(body).name;
      console.log(name);
    }
  });
  printCharacters(index + 1);
}
