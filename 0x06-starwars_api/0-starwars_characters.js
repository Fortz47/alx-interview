#!/usr/bin/node

const request = require('request');

function fetchCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

async function printCharacters () {
  if (process.argv.length < 3) return;

  const movieId = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  try {
    const movieResponse = await new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    for (const characterUrl of movieResponse.characters) {
      const characterName = await fetchCharacter(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

printCharacters();
