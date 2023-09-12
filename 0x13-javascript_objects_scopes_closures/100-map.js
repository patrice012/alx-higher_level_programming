#!/usr/bin/node

const list = require('./100-data').list;

function print (list) {
  console.log(list);
}

function factorIndex (list) {
  return list.map((element, index) => element * index);
}

const arr = factorIndex(list);

print(arr);
print(list);
