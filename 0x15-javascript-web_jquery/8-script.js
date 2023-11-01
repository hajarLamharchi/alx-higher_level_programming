$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $.each(data.results, function (index, movie) {
      const movieList = $('<li>').text(movie.title);
      $('#list_movies').append(movieList);
    });
  });
});
