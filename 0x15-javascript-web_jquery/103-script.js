$(document).ready(function () {
  $('#btn_translate').click(function () {
    const param = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + param, function (data) {
      $('#hello').text(data.hello);
    });
  });

  $('#language_code').keydown(function (event) {
    if (event.keyCode === 13) {
      const param = $('#language_code').val();
      $.get('https://hellosalut.stefanbohacek.dev/?lang=' + param, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
