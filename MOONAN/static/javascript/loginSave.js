
function toggleSave() {
    const checkImg = document.querySelector('.checkImg');
    const saveMessage = document.getElementById('saveMessage');


    checkImg.classList.toggle('active');

    if (checkImg.classList.contains('active')) {
        saveMessage.textContent = '로그인 정보 저장됨';
        saveMessage.style.color = "#FF003A";
        checkImg.src = "/static/image/redcheck.svg";
    } else {
        saveMessage.textContent = '로그인 정보 저장하기';
        saveMessage.style.color = "";
        checkImg.src = "/static/image/Group 1991.svg";
    }
}