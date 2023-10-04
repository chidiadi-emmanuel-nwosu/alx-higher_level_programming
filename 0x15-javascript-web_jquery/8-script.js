const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(url, (data) => {
  for (dt of data.results) {
    const list = $('<li>').text(dt.title);
    $('UL#list_movies').append(list);
  }
});
