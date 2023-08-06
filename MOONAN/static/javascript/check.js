// 사용 가능합니다 
function checkId() {
    var checkIdFeild = document.getElementById("idFeild");
    var checkText = document.querySelector(".checkTextId");
    var checkImg = document.querySelector(".checkImg");
    if(checkIdFeild.value.length > 0) {
        checkImg.src = "/static/image/redcheck.svg";
        checkText.style.color = "#FF003A";
    }
    else {
        checkImg.src = "/static/image/Group 1991.svg";
        checkText.style.color = "";
    }
}

function checkPassword() {
    var checkPasswordFeild = document.getElementById("passwordFeild");
    var checkText = document.querySelector(".checkTextPassword");
    var checkImg = document.querySelectorAll(".checkImg")[1];
    if(checkPasswordFeild.value.length >= 8) {
        checkImg.src = "/static/image/redcheck.svg";
        checkText.style.color = "#FF003A";
    }
    else {
        checkImg.src = "/static/image/Group 1991.svg";
        checkText.style.color = "";
    }
}

function checkPasswordRepeat() {
    var checkPasswordFeild = document.getElementById("passwordCheckFeild").value;
    var password = document.getElementById("passwordFeild").value;
    var checkImg = document.querySelectorAll(".checkImg")[2];
    var checkText = document.querySelector(".checkTextPasswordRepeat");
    if(password === checkPasswordFeild) {
        checkImg.src = "/static/image/redcheck.svg";
        checkText.style.color = "#FF003A";
        checkText.textContent = "비밀번호가 일치합니다."
    }
    else {
        checkImg.src = "/static/image/Group 2046.svg";
        checkText.style.color = "#08044E";
        checkText.textContent = "잘못된 비밀번호입니다.";
    }
}