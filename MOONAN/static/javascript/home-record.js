// 마이크 이미지 알림 
function mikeImgAlert() {
    alert("앱에서 확인해주세요.");
}

// let reasonOptionBox = document.querySelector(".reasonOptionBox");
function showdropdown(showImg) {
    let dropdownMenuBox = showImg.nextElementSibling;

    if(dropdownMenuBox.style.display === "none") {
        dropdownMenuBox.style.display = "block";
    }
    else {
        dropdownMenuBox.style.display = "none";
    }
}


// 완료 버튼 눌렀을 때 팝업
let savePopUp = document.getElementById("savePopUp");
savePopUp.style.display = "none";
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

// 페이스 선택화면 숨기거나 보이기 
let selectFace = document.querySelector(".selectReasonBox");
selectFace.style.display = "none";
function showReasonBox(emotion) {
    if(emotion === "sosoBox" || emotion === "badBox" || emotion === "worseBox") {
        selectFace.style.display = "flex";
    }
    else if (emotion === "goodBox" || emotion === "okayBox") {
        selectFace.style.display = 'none';
    }
} 

// 직접 입력 텍스트 변경
document.getElementById("directText").addEventListener("input", function() {
    const directTextValue = this.value;
    const titleDirectTextElement = document.getElementById("titleDirectText");
    titleDirectTextElement.textContent = directTextValue;
});