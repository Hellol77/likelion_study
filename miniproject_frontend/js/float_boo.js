var boos = document.querySelectorAll(".Boo");
for (var i = 0; i < boos.length; i++) {
  boos[i].addEventListener("click", select);
}

function select() {
  var boo = this.getAttribute("src");
  window.open("select_country.html?"+boo, "_self");
}
