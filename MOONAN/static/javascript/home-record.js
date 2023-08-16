// $(document).ready(function () {
//     $('.expressionImg').click(function () {
//         var expression = $(this).attr('id'); // 클릭된 이미지의 id 값
//         $.ajax({
//             type: 'POST',
//             url: '/home/record/', // 뷰 함수의 URL 경로
//             data: { 'expression': expression },
//             headers: { "X-CSRFToken": "{{ csrf_token }}" },
//             success: function (response) {
//                 // 성공적으로 처리된 경우의 동작
//                 let faceElements = document.querySelectorAll(".Face");
                
//                 faceElements.forEach((face) => {
//                     face.style.border = "none";
//                 });

//                 $(this).css("border", "3px solid var(--unnamed, #FF003A)");
//             },
//             error: function () {
//                 // 에러가 발생한 경우의 동작
//             }
//         });
//     });

//     // 선택한 표정 테두리 생기게 하기
//     let faceElements = document.querySelectorAll(".Face");

//     faceElements.forEach((face) => {
//         face.addEventListener('click', () => {
//             face.style.border = "3px solid var(--unnamed, #FF003A)";

//             faceElements.forEach((otherFace) => {
//                 if(otherFace !== face) {
//                     otherFace.style.border = "none";
//                 }
//             });
//         });
//     });
    
// });

// // 마이크 이미지 알림 
// function mikeImgAlert() {
//     alert("앱에서 확인해주세요.");
// }

// // 드랍다운 보기 
// let reasonMenuBox = document.querySelector(".reasonMenu");
// function showdropdown(showImg) {
//     let dropdownMenuBox = showImg.nextElementSibling;

//     if(dropdownMenuBox.style.display === "none") {
//         dropdownMenuBox.style.display = "block";
//     }
//     else {
//         dropdownMenuBox.style.display = "none";
//     }
// }

// // 선택한 표정에 따라 selectReasonBox 숨기기/보이기
// $(document).ready(function () {
//     // 기본적으로 페이지 로딩 시 reasonBox 숨기기
//     $('.reasonBox').hide();

//     // 선택한 표정에 따라 해당 reasonBox 보이기
//     $('.expressionImg').each(function () {
//         var expression = $(this).attr('id');
//         // '그럭저럭', '안좋아요', '나빠요' 선택 시 selectReasonBox 보이기
//         if (expression === 'sosoImg' || expression === 'badImg' || expression === 'worseImg') {
//             $(this).siblings('.reasonBox').show();
//         }
//     });

//     // '최고예요', '무난해요' 선택 시 selectReasonBox 숨기기
//     $('.expressionImg').click(function () {
//         $('.reasonBox').hide();

//         var expression = $(this).attr('id');
//         if (expression === 'sosoImg' || expression === 'badImg' || expression === 'worseImg') {
//             $(this).siblings('.reasonBox').show();
//         }
//     });
// });


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

// 각각의 li 요소에 클릭 이벤트를 추가
document.querySelectorAll('.reasonMenuOption li').forEach((item) => {
    item.addEventListener('click', function () {
        // 클릭한 항목의 텍스트 내용 가져오기
        const selectedText = this.textContent;
        
        // 해당하는 reasonMenuText 엘리먼트 찾기
        const reasonMenuTextElement = this.closest('.reasonOptionBox').querySelector('.reasonMenuText');
        
        // reasonMenuText에 선택한 텍스트 내용 반영하기
        reasonMenuTextElement.textContent = selectedText;
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
