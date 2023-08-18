function addList() {
    const addValue = document.getElementById('customContentInput').value;

    const li = document.createElement("li");
    const textNode = document.createTextNode(addValue);
    li.appendChild(textNode);

    const ul = document.querySelector('.munan-menu-list-detail');
    const referenceLi = document.querySelector('.munan-menu-list-detail li:last-child');
    ul.insertBefore(li, referenceLi);

    document.getElementById('customContentInput').value = '';

    li.addEventListener("click", function() {
        updateMunanText(this);
    });

    // 추가한 내용을 customContent에 할당
    const customContentInput = document.getElementById('customContentInput');
    customContentInput.value = addValue;
}

// 드롭다운 메뉴 보이기/숨기기 함수
function showdropdown(showImg) {
    let dropdownMenuBox = showImg.nextElementSibling;

    if (dropdownMenuBox) {
        if(dropdownMenuBox.style.display === "none") {
            dropdownMenuBox.style.display = "block";
        } else {
            dropdownMenuBox.style.display = "none";
        }
    } else {
        console.log("Dropdown menu box not found.");
    }
}

// 완료 버튼 눌렀을 때 팝업
let savePopUp = document.getElementById("savePopUp");
if (savePopUp) {
    savePopUp.style.display = "none";
}

function showSavePopUp() {
    if(savePopUp.style.display === "none") {
        savePopUp.style.display = "flex";
        $('#expressionForm').submit();
    }
}

function closeSavePopUp() {
    savePopUp.style.display = "none";
    window.location.href = "/home";
}
