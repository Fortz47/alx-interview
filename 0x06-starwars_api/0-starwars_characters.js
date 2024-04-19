#!/usr/bin/node

const request = require('request');

function print_characters() {
	if (process.argv.length < 2) return;
	const movie_id = process.argv[1];
	const url = 'https://swapi-api.alx-tools.com/api/films/' + movie_id + '/';
	request(url, (err, res, body) => {
		if (err) {
			console.error('Error:', err);
			return;
		}
		JSON.parse(body).characters.forEach((character_url) => {
			request(character_url, (err, res, body) => {
				if (err) {
					console.error('Error:', err);
					return;
				}
				console.log(JSON.parse(body).name);
			});
		});
	});
};
