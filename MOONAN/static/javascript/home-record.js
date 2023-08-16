// 선택한 표정 테두리 생기게 하기
let faceElements = document.querySelectorAll(".Face");

faceElements.forEach((face) => {
    face.addEventListener('click', () => {
        face.style.border = "3px solid var(--unnamed, #FF003A)";

        faceElements.forEach((otherFace) => {
            if(otherFace !== face) {
                otherFace.style.border = "none";
            }
        });
    });
});

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

// 각각의 li 요소에 클릭 이벤트를 추가
document.querySelectorAll('.reasonMenuOption li').forEach((item) => {
    item.addEventListener('click', function () {
        // 클릭한 항목의 텍스트 내용 가져오기
        const selectedText = this.textContent;
        
        // 해당하는 reasonMenuText 엘리먼트 찾기
        const reasonMenuTextElement = this.closest('.reasonOptionBox').querySelector('.reasonMenuText');
        
        // reasonMenuText에 선택한 텍스트 내용 반영하기
        reasonMenuTextElement.textContent = selectedText;
        reasonMenuTextElement.style.color = "#FF003A";
    });
});

$(document).ready(function() {
    // 선택한 표정 버튼 클릭 시
    $('.expressionImg').click(function() {
        const expression = $(this).attr('id');
        $.ajax({
            type: 'POST',
            url: '/home/record/submit_expression/',
            data: { expression: expression, csrfmiddlewaretoken: csrfToken },
            dataType: 'json',
            success: function(response) {
                console.log('표정 선택 성공:', response);
                // 선택한 표정에 대한 동작 수행
            },
            error: function(error) {
                console.error('표정 선택 오류:', error);
            }
        });
    });

    // 이유 카테고리 선택 시 (같은 방식으로 처리)
    $('.reasonMenuOption li').click(function() {
        const selectedCategory = $(this).data('category');
        const selectedReason = $(this).text();  // 선택한 이유
    
        $.ajax({
            type: 'POST',
            url: '/home/record/submit_reason/',  // 절대 경로로 수정
            data: { category: selectedCategory, reason: selectedReason, csrfmiddlewaretoken: csrfToken },
            dataType: 'json',
            success: function(response) {
                console.log(selectedCategory+selectedReason+'이유 선택 성공:', response);
                // 선택한 이유에 대한 동작 수행
            },
            error: function(error) {
                console.error('이유 선택 오류:', error);
            }
        });
    });
    

    // 직접 입력 텍스트 전송 시 (같은 방식으로 처리)
    $('#directTextSubmit').click(function() {
        const directReason = $('#directText').val();
        if (directReason) {
            $.ajax({
                type: 'POST',
                url: '{% url "record:submit_reason" %}',
                data: { reason: directReason, csrfmiddlewaretoken: csrfToken },
                dataType: 'json',
                success: function(response) {
                    console.log('직접 입력 성공:', response);
                    // 선택한 이유에 대한 동작 수행
                },
                error: function(error) {
                    console.error('직접 입력 오류:', error);
                }
            });
        }
    });

    // 입력 완료 버튼 클릭 시 (같은 방식으로 처리)
    $('.inputCompletedButton').click(function() {
        const selectedReason = $('.reasonMenuOption li input:checked').val();
        if (selectedReason) {
            $.ajax({
                type: 'POST',
                url: '{% url "record:submit_reason" %}',
                data: { reason: selectedReason, csrfmiddlewaretoken: csrfToken },
                dataType: 'json',
                success: function(response) {
                    console.log('이유 선택 성공:', response);
                    // 선택한 이유에 대한 동작 수행
                },
                error: function(error) {
                    console.error('이유 선택 오류:', error);
                }
            });
        }
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
}

// 페이스 선택화면 숨기거나 보이기 
let selectFace = document.querySelector(".selectReasonBox2");
selectFace.style.display = "none";
function showReasonBox(emotion) {
    if(emotion === "sosoBox" || emotion === "badBox" || emotion === "worseBox") {
        selectFace.style.display = "flex";
    }
    else if (emotion === "goodBox" || emotion === "okayBox") {
        selectFace.style.display = 'none';
    }
} 