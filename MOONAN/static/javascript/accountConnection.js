// 연결할 아이디 추가하기
let currentConnectionNumber = 1;
function addId() {
    let idBox = document.querySelector(".connectIdBox");
    let clone = idBox.cloneNode(true);
    var inputField = clone.querySelector("#idFeild");
    inputField.value = "";
    currentConnectionNumber++;
    clone.querySelector(".connectionNumber").textContent = currentConnectionNumber; 
    
    let beAdded = document.querySelector(".beAdded");
    beAdded.appendChild(clone);
}