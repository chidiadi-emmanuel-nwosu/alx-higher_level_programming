#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const args = process.argv.slice(2);

request.get(args[0], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(args[1], response.body, 'utf-8', (err) => {
        if (err) {
          console.log(err);
        }
      });
    }
  }
});
