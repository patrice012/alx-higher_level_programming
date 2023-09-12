#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const arr = list.filter((ele) => ele === searchElement);
  return arr.length;
};
