var overlapButton = document.getElementById("overlap-button");
overlapButton.addEventListener("click", function (event) {
    event.preventDefault(); // 기본 동작 중지
    window.location.href = "/accountConnection.html"; // 페이지 이동
});

function updateMunanText(clickedListItem) {
    var selectedText = clickedListItem.innerText;
    var munanTextElement = document.querySelector('.munan-list-text');
    munanTextElement.textContent = selectedText;

    munanTextElement.style.color = "#FF003A"; // 선택지에 해당하는 색상 또는 기본 색상 적용
    munanTextElement.style.fontWeight = "700";
}

function addList() {
    const addValue = document.getElementById('addValue').value;

    if (addValue.trim() === '') {
        alert('추가할 값을 입력하세요.');
        return;
    }

    const li = document.createElement("li");

    const textNode = document.createTextNode(addValue);
    li.appendChild(textNode);

    const ul = document.querySelector('.munan-menu-list-detail');
    const referenceLi = document.querySelector('.munan-menu-list-detail li:nth-child(6)');
    ul.insertBefore(li, referenceLi); // 오름차순으로 추가

    document.getElementById('addValue').value = '';

    li.addEventListener("click", function() {
        updateMunanText(this);
    });
}

// 드랍다운 보기 
let reasonMenuBox = document.querySelector(".reasonMenu");
function showdropdown(showImg) {
    let dropdownMenuBox = showImg.nextElementSibling;

    if(dropdownMenuBox.style.display === "none") {
        dropdownMenuBox.style.display = "block";
    }
    else {
        dropdownMenuBox.style.display = "none";
    }
}