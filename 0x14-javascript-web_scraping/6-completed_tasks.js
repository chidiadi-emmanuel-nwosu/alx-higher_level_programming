#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request.get(args[0], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      const users = {};
      const data = JSON.parse(body);

      data.forEach(element => {
        const count = data.filter(e => e.userId === element.userId && e.completed);
        users[element.userId] = count.length;
      });

      console.log(users);
    }
  }
});
