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

// 클릭 이벤트에 따른 선택된 데이터를 저장할 객체 초기화
const selectedData = {};

document.querySelectorAll('.reasonMenuOption li').forEach((item) => {
    item.addEventListener('click', function () {
        // 클릭한 항목의 텍스트 내용 가져오기
        const selectedText = this.textContent;
        
        // 해당하는 reasonMenuText 엘리먼트 찾기
        const reasonMenuTextElement = this.closest('.reasonOptionBox').querySelector('.reasonMenuText');
        
        // reasonMenuText에 선택한 텍스트 내용 반영하기
        reasonMenuTextElement.textContent = selectedText;
        reasonMenuTextElement.style.color = "#FF003A";

        // 선택된 항목에 selected 클래스 부여하기
        document.querySelectorAll('.reasonMenuText').forEach((textElement) => {
            textElement.classList.remove('selected'); // 다른 항목의 selected 클래스 제거
        });
        reasonMenuTextElement.classList.add('selected'); // 선택한 항목에 selected 클래스 부여

        // 선택된 카테고리 가져오기
        const selectedCategory = reasonMenuTextElement.getAttribute('id');
        
        // 객체에 선택된 카테고리와 이유 저장
        selectedData[selectedCategory] = selectedText;

        // 저장된 데이터 출력 
        console.log("선택한 이유:" ,selectedData);
    });
});



$(document).ready(function() {
    // 선택한 표정 테두리 생기게 하기
    $('.Face').click(function() {
        $('.Face').css('border', 'none'); // 모든 표정의 테두리 초기화
        $(this).css('border', '3px solid var(--unnamed, #FF003A)'); // 선택한 표정의 테두리 설정
    });

    // 폼 제출 이벤트 핸들러
    $('#expressionForm').submit(function(event) {
        event.preventDefault();  // 기본 폼 제출 동작 막기
        
        const expression = $('.Face').filter(function() {
            return $(this).css('border') === '3px solid rgb(255, 0, 58)';
        }).find('.expressionImg').attr('id');

        const directReason = $('#directText').val();

        // 선택된 데이터를 JSON 형식으로 변환
        const jsonData = JSON.stringify(selectedData);

        console.log('표정:', expression);
        console.log('직접 쓴 이유:', directReason);
        
        $.ajax({
            type: 'POST',
            url: '/home/record/submit_data/',  
            data: {
                expression: expression,
                selectedData: jsonData,
                customReason: directReason,
                csrfmiddlewaretoken: csrfToken
            },
            dataType: 'json',
            success: function(response) {
                console.log('데이터 제출 성공:', response);
            },
            error: function(error) {
                console.error('데이터 제출 오류:', error);
            }
        });
    });
});

// 완료 버튼 눌렀을 때 팝업
let savePopUp = document.getElementById("savePopUp");
savePopUp.style.display = "none";
function showSavePopUp() {
    if(savePopUp.style.display === "none") {
        event.preventDefault();
        savePopUp.style.display = "flex";
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