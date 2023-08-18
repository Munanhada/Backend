// 사용 가능합니다 
function checkId() {
    var checkIdField = document.getElementById("idField");
    var checkText = document.querySelector(".checkTextId");
    var checkImg = document.querySelector(".checkImg");

    $("input[name='user_id']").on("change", function() {
        var user_id = checkIdField.value;

        // AJAX 호출
        $.ajax({
            type: 'POST', 
            url: '/accounts/id_check/',
            data: {user_id: user_id},
            dataType:'json',
            success: function(response) {
                if (response.result != 'success') {
                    return;
                }  

                if (response.data === 'exist') {
                    // user_id가 이미 존재할 경우
                    checkImg.src = "/static/image/Group 1991.svg";
                    checkText.style.color = "";
                } else {
                    // user_id가 중복되지 않는 경우
                    checkImg.src = "/static/image/redcheck.svg";
                    checkText.style.color = "#FF003A";
                }
            },
            error : function(error) { // AJAX 요청이 실패한 경우 처리
                    alert("AJAX 요청이 실패했습니다.");
                    console.error("error : " + error);
            }
        });
    });
}

function checkPassword() {
    var checkPasswordFeild = document.getElementById("passwordFeild");
    var checkText = document.querySelector(".checkTextPassword");
    var checkImg = document.querySelectorAll(".checkImg")[1];
    if(checkPasswordFeild.value.length >= 1) {
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