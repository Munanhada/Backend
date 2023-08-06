// 비밀번호 보기
function togglePasswordVisiblity() {
    var passwordFeild = document.getElementById("passwordFeild");
    var toggleImg1 = document.querySelector(".hiddenImg1");
    if(passwordFeild.type === "password") {
        passwordFeild.type = "type";
        toggleImg1.src = "/static/image/Group 2026.svg"; 
    }
    else {
        passwordFeild.type = "password";
        toggleImg1.src = "/static/image/Visibility off.svg";
    }
}

function togglePasswordCheckVisiblity() {
    var passwordFeild = document.getElementById("passwordCheckFeild");
    var toggleImg2 = document.querySelector(".hiddenImg2");
    if(passwordFeild.type === "password") {
        passwordFeild.type = "type";
        toggleImg2.src = "/static/image/Group 2026.svg";
    }
    else {
        passwordFeild.type = "password";
        toggleImg2.src = "/static/image/Visibility off.svg";
    }
}