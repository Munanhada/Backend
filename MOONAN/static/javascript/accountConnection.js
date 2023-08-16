// 연결할 아이디 추가하기
let currentConnectionNumber = 1;
let addedDivs = [];
function addId() {
    let idBox = document.querySelector(".connectBox");
    let clone = idBox.cloneNode(true);
    var inputField = clone.querySelectorAll(".famIdField");
    let inputField2 = clone.querySelectorAll(".famIdField2");
    inputField.forEach(function (inputField) {
        inputField.value = "";
    });
    inputField2.forEach(function (inputField2) {
        inputField2.value = "";
    });
    currentConnectionNumber++;
    clone.querySelector(".connectionNumber").textContent = currentConnectionNumber;

    let beAdded = document.querySelector(".beAdded");
    clone.classList.add("addedConnection" + currentConnectionNumber);
    beAdded.appendChild(clone);
    addedDivs.push(clone);

    let dropdownOptions = clone.querySelectorAll(".dropdownOption");
    dropdownOptions.forEach(option => {
        option.classList.remove("selected");
        option.style.color = "var(--unnamed, #17181A)";
    });

    let selectedText = clone.querySelector(".selectText");
    selectedText.textContent = "선택";
    selectedText.style.color = "#959AA4";

    let clonedropdown = clone.querySelector(".dropdownBox");
    clonedropdown.style.display = "none";

    let dropdownOption2 = clone.querySelectorAll(".dropdownOption2");
    dropdownOption2.forEach(option => {
        option.classList.remove("selected");
        option.style.color = "var(--unnamed, #17181A)";
    });

    let selectedText2 = clone.querySelector(".selectText2");
    selectedText2.textContent = "선택";
    selectedText2.style.color = "#959AA4";

    let clonedropdown2 = clone.querySelector(".dropdownBox2");
    clonedropdown2.style.display = "none";
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

// 선택된 요소 색 변경 
// let dropdownOptions = document.querySelectorAll(".dropdownOption");
// let selectedText = document.querySelector(".selectText")
// dropdownOptions.forEach(option => {
//     option.addEventListener('click', function() {
//         if (!option.classList.contains("selected")) { // 이미 선택되지 않은 경우에만 처리
//             dropdownOptions.forEach(otherOption => {
//                 otherOption.classList.remove("selected"); // 다른 항목들의 선택 클래스 제거
//                 otherOption.style.color = "var(--unnamed, #17181A)"; // 다른 항목들의 색상 원래대로 변경
//             });

//             option.classList.add("selected"); // 선택한 항목에 선택 클래스 추가
//             option.style.color = "#FF003A"; // 선택한 항목의 색상 변경
//             selectedText.textContent = option.textContent;
//             selectedText.style.color = "#17181A";
//         }
//     });
// });


// let dropdownOptions2 = document.querySelectorAll(".dropdownOption2");
// let selectedText2 = document.querySelector(".selectText2")
// dropdownOptions2.forEach(option2 => {
//     option2.addEventListener('click', function () {
//         if (!option2.classList.contains("selected")) { // 이미 선택되지 않은 경우에만 처리
//             dropdownOptions2.forEach(otherOption2 => {
//                 otherOption2.classList.remove("selected"); // 다른 항목들의 선택 클래스 제거
//                 otherOption2.style.color = "var(--unnamed, #17181A)"; // 다른 항목들의 색상 원래대로 변경
//             });

//             option2.classList.add("selected"); // 선택한 항목에 선택 클래스 추가
//             option2.style.color = "#FF003A"; // 선택한 항목의 색상 변경
//             selectedText2.textContent = option2.textContent;
//             selectedText2.style.color = "#17181A";
//         }
//     });
// });

// 드랍다운 표시 
// let dropdown = document.querySelector(".dropdownBox");
// dropdown.style.display = "none";
// function showDropdown(dropdownImg) {
//     let dropdownBox = dropdownImg.nextElementSibling; 

//     if (dropdownBox.style.display === "none") {
//         dropdownBox.style.display = "block";
//     } else {
//         dropdownBox.style.display = "none";
//     }
    
//     let dropdownOptions = document.querySelectorAll(".dropdownOption");
//     let selectedText = dropdownImg.parentElement.querySelector(".selectText"); // 수정된 부분
//     dropdownOptions.forEach(option => {
//         option.addEventListener('click', function () {
//             if (!option.classList.contains("selected")) {
//                 let parentBox = option.closest(".connectBox"); // 수정된 부분
//                 let parentSelectedText = parentBox.querySelector(".selectText"); // 수정된 부분

//                 dropdownOptions.forEach(otherOption => {
//                     otherOption.classList.remove("selected");
//                     otherOption.style.color = "var(--unnamed, #17181A)";
//                 });

//                 option.classList.add("selected");
//                 option.style.color = "#FF003A";
//                 selectedText.textContent = option.textContent;
//                 selectedText.style.color = "#17181A";
                
//                 parentSelectedText.textContent = option.textContent; // 수정된 부분
//                 parentSelectedText.style.color = "#17181A"; // 수정된 부분
//             }
//         });
//     });

//     for (let i = 0; i<addedDivs.length; i++) {
//         let cloneSelctedTextDiv = addedDivs[i];
//         let cloneSelctedText = cloneSelctedTextDiv.querySelector(".selectText");
//         let cloneDropdownOption = cloneSelctedTextDiv.querySelectorAll(".dropdownOption");
//         cloneDropdownOption.forEach(menu => {
//             menu.addEventListener('click', function () {
//                 cloneSelctedText.textContent = menu.textContent;
//                 cloneSelctedText.style.color = "#17181A";
//             })
//         })
//     }
// }

// let dropdown2 = document.querySelector(".dropdownBox2");
// dropdown2.style.display = "none";
// function showDropdown2(dropdownImg2) {
//     let dropdownBox = dropdownImg2.nextElementSibling;

//     if (dropdownBox.style.display === "none") {
//         dropdownBox.style.display = "block";
//     }
//     else {
//         dropdownBox.style.display = "none";
//     }
//     let dropdownOptions2 = document.querySelectorAll(".dropdownOption2");
//     let selectedText2 = dropdownImg2.parentElement.querySelector(".selectText2"); // 수정된 부분
//     dropdownOptions2.forEach(option2 => {
//         option2.addEventListener('click', function () {
//             if (!option2.classList.contains("selected")) {
//                 let parentBox = option2.closest(".connectBox"); // 수정된 부분
//                 let parentSelectedText = parentBox.querySelector(".selectText2"); // 수정된 부분

//                 dropdownOptions2.forEach(otherOption2 => {
//                     otherOption2.classList.remove("selected");
//                     otherOption2.style.color = "var(--unnamed, #17181A)";
//                 });

//                 option2.classList.add("selected");
//                 option2.style.color = "#FF003A";
//                 selectedText2.textContent = option2.textContent;
//                 selectedText2.style.color = "#17181A";
                
//                 parentSelectedText.textContent = option2.textContent; // 수정된 부분
//                 parentSelectedText.style.color = "#17181A"; // 수정된 부분
//             }
//         });
//     });

//     for (let i = 0; i<addedDivs.length; i++) {
//         let cloneSelctedTextDiv2 = addedDivs[i];
//         let cloneSelctedText2 = cloneSelctedTextDiv2.querySelector(".selectText2");
//         let cloneDropdownOption2 = cloneSelctedTextDiv2.querySelectorAll(".dropdownOption2");
//         cloneDropdownOption2.forEach(menu => {
//             menu.addEventListener('click', function () {
//                 cloneSelctedText2.textContent = menu.textContent;
//                 cloneSelctedText2.style.color = "#17181A";
//             })
//         })
//     }
// }

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

