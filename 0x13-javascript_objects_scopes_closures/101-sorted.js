#!/usr/bin/node

const dict = require('./101-data').dict;

function sortedOccurences () {
  const keys = Object.keys(dict);
  const values = Object.values(dict);
  const data = {};

  for (let i = 0; i < values.length; i++) {
    if (values[i] in Object.keys(data)) {
      data[values[i]].push(keys[i]);
    } else {
      data[values[i]] = [keys[i]];
    }
  }

  return data;
}

console.log(sortedOccurences());
