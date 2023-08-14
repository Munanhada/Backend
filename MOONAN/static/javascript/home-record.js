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