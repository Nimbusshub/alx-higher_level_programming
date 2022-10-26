$(function () {
  const apiUrl = "https://stefanbohacek.com/hellosalut/?lang=fr";
  $.get(apiUrl, function (data) {
    $("DIV#hello").text(data.hello);
  });
});
