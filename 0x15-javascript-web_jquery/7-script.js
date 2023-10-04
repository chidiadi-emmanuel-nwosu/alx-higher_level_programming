const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.getJSON(url, (data) => $('DIV#character').text(data.name));
