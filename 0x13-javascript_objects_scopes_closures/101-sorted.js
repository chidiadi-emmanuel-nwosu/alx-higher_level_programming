#!/usr/bin/node

/* import a diction from an external file */
const dict = require('./101-data').dict;

/* declare an empty dictionary */
const newDict = {};

/* iterate over the dictionary keys and create and add values to newDict */
Object.keys(dict).forEach(key => {
  const value = dict[key];
  if (!newDict[value]) { newDict[value] = []; }
  newDict[value].push(key);
});

/* output the newDict */
console.log(newDict);
