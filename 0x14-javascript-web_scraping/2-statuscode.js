#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request.get(args[0], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
