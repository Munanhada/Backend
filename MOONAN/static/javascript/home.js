var overlapButton = document.getElementById("overlap-button");
overlapButton.addEventListener("click", function (event) {
    event.preventDefault(); // 기본 동작 중지
    window.location.href = "/accountConnection.html"; // 페이지 이동
});

function updateMunanText(clickedListItem) {
    var selectedText = clickedListItem.innerText;
    var munanTextElement = document.querySelector('.munan-list-text');
    munanTextElement.textContent = selectedText;

    munanTextElement.style.color = "#FF003A";
    munanTextElement.style.fontWeight = "700";
}

function addList() {
    const addValue = document.getElementById('addValue').value;

    const li = document.createElement("li");
    const textNode = document.createTextNode(addValue);
    li.appendChild(textNode);

    const ul = document.querySelector('.munan-menu-list-detail');
    const referenceLi = document.querySelector('.munan-menu-list-detail li:last-child');
    ul.insertBefore(li, referenceLi);

    document.getElementById('addValue').value = '';

    li.addEventListener("click", function() {
        updateMunanText(this);
    });
}