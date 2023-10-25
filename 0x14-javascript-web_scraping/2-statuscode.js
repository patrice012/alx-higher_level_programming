#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url).on('response', function (response) {
  console.log(response);
  console.log(`code: ${response.statusCode}`);
}).on('error', function (error) {
  console.log(error);
});
