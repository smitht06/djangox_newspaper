//load the randomized stats into create character form (create_character.html)
document.addEventListener('DOMContentLoaded', function () {
	const randomizeButton = document.getElementById('randomize-stats');
	randomizeButton.addEventListener('click', function () {
		// Call the backend view to generate random stats
		fetch('/character/generate_random_stats/')
			.then((response) => response.json())
			.then((data) => {
				// Update the form fields with the random stats
				document.getElementById('id_strength').value = data.strength;
				document.getElementById('id_dexterity').value = data.dexterity;
				document.getElementById('id_constitution').value =
					data.constitution;
				document.getElementById('id_intelligence').value =
					data.intelligence;
				document.getElementById('id_wisdom').value = data.wisdom;
				document.getElementById('id_charisma').value = data.charisma;
			});
	});
});
