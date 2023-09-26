#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(`${url}${args[0]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      const data = JSON.parse(body).characters;

      data.forEach(element => {
        request.get(element, (err, response, body) => {
          if (err) {
            console.log(err);
          } else {
            if (response.statusCode === 200) {
              const name = JSON.parse(body).name;
              console.log(name);
            }
          }
        });
      });
    }
  }
});
