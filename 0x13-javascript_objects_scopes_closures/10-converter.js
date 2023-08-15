#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    let ret = '';
    do {
      ret += (number % base).toString();
      number = Math.floor(number / base);
    } while (number > 0);
    return ([...ret].reverse().join(''));
  };
};
