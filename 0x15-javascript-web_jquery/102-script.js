$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    if (languageCode) {
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

      $.getJSON(apiUrl, function (data) {
        const translation = data.hello;
        $('DIV#hello').text(translation);
      });
    }
  });
});
