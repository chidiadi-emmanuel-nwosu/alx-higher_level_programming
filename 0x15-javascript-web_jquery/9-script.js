const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(document).ready(() => {
  $.getJSON(url, (data) => {
    $('DIV#hello').text(data.hello);
  });
});
