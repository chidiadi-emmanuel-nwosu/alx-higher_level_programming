#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (const element of list) {
    element === searchElement && occur++;
  }
  return (occur);
};
