#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request.get(args[0], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      const results = data.results;

      const num = results.map(
        x => x.characters
      ).filter(x => x.some(x => x.includes(18)));

      console.log(num.length);
    }
  }
});
