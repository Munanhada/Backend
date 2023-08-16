var selectElement = document.getElementById("birthYear");
  
for (var i = 2023; i >= 1900; i--) {
  var option = document.createElement("option");
  option.value = i;
  option.text = i;
  selectElement.appendChild(option);
}