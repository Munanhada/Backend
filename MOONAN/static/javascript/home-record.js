$(document).ready(function () {
    $('.expressionImg').click(function () {
        var expression = $(this).attr('id'); // 클릭된 이미지의 id 값
        $.ajax({
            type: 'POST',
            url: '/home/record/', // 뷰 함수의 URL 경로
            data: { 'expression': expression },
            success: function (response) {
                // 성공적으로 처리된 경우의 동작
                let faceElements = document.querySelectorAll(".Face");
                
                faceElements.forEach((face) => {
                    face.style.border = "none";
                });

                $(this).css("border", "3px solid var(--unnamed, #FF003A)");
            },
            error: function () {
                // 에러가 발생한 경우의 동작
            }
        });
    });

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
});
