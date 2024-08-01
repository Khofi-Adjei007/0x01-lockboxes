#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Retrieve the film ID from the command-line arguments
const filmId = process.argv[2];

// Construct the URL for the Star Wars API to fetch details about the film
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

// Make a request to the Star Wars API to get information about the specified film
request(url, async (err, response, body) => {
  if (err) {
    // If there's an error with the request, log the error and exit
    console.log(err);
    return;
  }

  // Parse the response body to get the list of character URLs
  const characters = JSON.parse(body).characters;

  // Loop through each character URL
  for (const characterUrl of characters) {
    // Use an async function to make the request for each character
    await new Promise((resolve, reject) => {
      // Make a request to get details about the character
      request(characterUrl, (err, response, body) => {
        if (err) {
          // If there's an error with the request, reject the promise
          reject(err);
          return;
        }

        // Parse the response body to get the character's name and log it
        console.log(JSON.parse(body).name);

        // Resolve the promise to indicate the request is complete
        resolve();
      });
    });
  }
});
