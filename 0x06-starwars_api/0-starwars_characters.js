#!/usr/bin/node

const request = require("request");

const movieNum = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieNum}`;

// Makes API request, sets async to allow await promise
request(URL, async function (err, res, body) {
  if (err) return console.error(err);

  // parse each character in the film as a list objects
  const charURLList = JSON.parse(body).characters;

  // Use URL list to character pages to make new requests
  // await queues requests until they resolve in order
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // finds each character name and prints in URL order
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
