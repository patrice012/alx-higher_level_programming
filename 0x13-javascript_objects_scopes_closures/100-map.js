#!/usr/bin/node

const list = require('./100-data').list;

const arr = [];
list.map((item, index) => arr.push(item * index));

console.log(list);
console.log(arr);

