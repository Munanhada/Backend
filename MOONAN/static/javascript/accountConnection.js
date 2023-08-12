// 연결할 아이디 추가하기
let currentConnectionNumber = 1;
function addId() {
    let idBox = document.querySelector(".connectBox");
    let clone = idBox.cloneNode(true);
    var inputField = clone.querySelectorAll("#famIdField");
    inputField.forEach(function(inputField) {
        inputField.value = "";
    });
    currentConnectionNumber++;
    clone.querySelector(".connectionNumber").textContent = currentConnectionNumber;

    let beAdded = document.querySelector(".beAdded");
    beAdded.appendChild(clone);
}

document.getElementById("popUp").style.display = "none";


function skip() {
    let popup = document.getElementById("popUp");
    if (popup.style.display === "none") {
        event.preventDefault();
        popup.style.display = "flex";
    }
}

function closePopup() {
    let popup = document.getElementById("popUp");
    popup.style.display = "none";
}