#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();

console.log(r1.width, r1.height);
r1.print();

console.log('Rotate:');
r1.rotate();
console.log(r1.width, r1.height);
r1.print();
