#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];

  for (let index = 0; index < list.length; index++) {
    arr.unshift(list[index]);
  }
  return arr;
};
