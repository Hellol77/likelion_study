let temp = location.href.split("?");

var countries = document.querySelectorAll(".Country");
for (var i = 0; i < countries.length; i++) {
  countries[i].addEventListener("click", select);
}

function select() {
  var country = this.getAttribute("src");
  window.open("decorate_boo?"+temp[1]+"?"+country, "_self");
}
