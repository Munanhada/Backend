// 연결할 아이디 추가하기
let currentConnectionNumber = 1;
let addedDivs = [];
// let clearImg = document.querySelector(".clearImg");
// clearImg.style.display = "none";
function addId() {
    let idBox = document.querySelector(".connectBox");
    let clone = idBox.cloneNode(true); // 기존 요소를 복제하여 새로운 요소 생성
    var inputField = clone.querySelectorAll(".famIdField");
    let inputField2 = clone.querySelectorAll(".famIdField2");
    
    // 1. famIdField class 의 name 변경
    currentConnectionNumber++; //연결 계정 번호 증가
    inputField.forEach(function (inputField) {
        inputField.value = "";
        inputField.name = "to_user" + currentConnectionNumber; // name 속성 변경
    });
    inputField2.forEach(function (inputField2) {
        inputField2.value = "";
    });
    clone.querySelector(".connectionNumber").textContent = currentConnectionNumber;

    //select 태그 name 변경
    var inputField = clone.querySelectorAll(".hello");
    inputField.forEach(function (selectField) {
        selectField.name = "relationship2_" + currentConnectionNumber;
    });

    var inputField = clone.querySelectorAll(".hello2");
    inputField.forEach(function (selectField) {
        selectField.name = "relationship1_" + currentConnectionNumber;
    });    

    let beAdded = document.querySelector(".totalConnectBox");
    clone.classList.add("addedConnection" + currentConnectionNumber);
    beAdded.appendChild(clone);
    addedDivs.push(clone);

    
    if(currentConnectionNumber == 3){
        let addId = document.querySelector(".addBox");
        addId.style.display = 'none';
    }

    // 삭제 버튼
    let deleteButton = clone.querySelector(".clearImg");
    deleteButton.addEventListener("click", function() {
        let listItem = deleteButton.closest(".connectBox");
        listItem.remove();
        currentConnectionNumber--;
        let addId = document.querySelector(".addBox");
        addId.style.display = 'flex';
    });
}



// 팝업 보이기 와 가리기
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


// 연결할 아이디 받아오기
function cloneFamId(inputField) {
    let famId = document.querySelector(".famIdField").value;
    let famId2 = document.querySelector(".famIdField2");
    famId2.value = famId;
    for (let i = 0; i < addedDivs.length; i++) {
        let currentDiv = addedDivs[i];
        let cloneFamId = currentDiv.querySelector(".famIdField").value;
        let cloneFamId2 = currentDiv.querySelector(".famIdField2");
        cloneFamId2.value = cloneFamId;
    }
}

// select 색 변격
function changeColor(selectElement, otherSelectId) {
    var selectedOption = selectElement.options[selectElement.selectedIndex];
    var otherSelect = document.getElementById(otherSelectId);

    // 변경된 select의 색상을 빨간색으로 변경
    selectElement.style.color = '#17181A';

    // 다른 select의 색상을 원래대로 변경
    otherSelect.style.color = '';

    // 선택된 옵션을 다른 select에 복사
    var otherSelectOption = otherSelect.querySelector('option[value="' + selectedOption.value + '"]');
    if (otherSelectOption) {
        otherSelectOption.selected = true;
    }
}