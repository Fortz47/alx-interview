#!/usr/bin/node

const request = require('request');

function fetchCharacter(character_url) {
  return new Promise((resolve, reject) => {
    request(character_url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

async function print_characters() {
  if (process.argv.length < 3) return;

  const movie_id = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}/`;

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

print_characters();
