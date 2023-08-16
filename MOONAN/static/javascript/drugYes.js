// document.addEventListener("DOMContentLoaded", function () {
//     const medicationInput = document.getElementById("medication-input");
//     const medicationList = document.getElementById("medication-list");

//     const nutritionInput = document.getElementById("nutrition-input");
//     const nutritionList = document.getElementById("nutrition-list");

//     function addMedicationButton(medicationName) {
//         const medicationButton = document.createElement("button");
//         medicationButton.type = "button";
//         medicationButton.name = "medication_choice";
//         medicationButton.value = medicationName;
//         medicationButton.textContent = medicationName;
//         medicationList.appendChild(medicationButton);
//         medicationInput.value = "";
//     }

//     function addNutritionButton(nutritionName) {
//         const nutritionButton = document.createElement("button");
//         nutritionButton.type = "button";
//         nutritionButton.name = "nutrition_choice";
//         nutritionButton.value = nutritionName;
//         nutritionButton.textContent = nutritionName;
//         nutritionList.appendChild(nutritionButton); 
//         nutritionInput.value = "";
//     }

//     // "복용중인 약" 입력 외부 영역 클릭 시
//     document.addEventListener("click", function (event) {
//         if (!medicationInput.contains(event.target) && !medicationList.contains(event.target)) {
//             const newMedication = medicationInput.value.trim();
//             if (newMedication !== "") {
//                 addMedicationButton(newMedication);
//             }
//         }
//     });

//     // "복용중인 영양제" 입력 외부 영역 클릭 시
//     document.addEventListener("click", function (event) {
//         if (!nutritionInput.contains(event.target) && !nutritionList.contains(event.target)) {
//             const newNutrition = nutritionInput.value.trim();
//             if (newNutrition !== "") {
//                 addNutritionButton(newNutrition);
//             }
//         }
//     });
// });

// // ajax 요청을 보내는 함수
// function updateMedicationChoices(newMedication) {
//     $.ajax({
//         url: "/add_medication/",
//         method: "POST",
//         data: { new_medication: newMedication, csrfmiddlewaretoken: csrfToken },
//         dataType: "json",
//         success: function (data) {
//             // 업데이트된 선택지를 화면에 반영
//             $.each(data.medication_list, function (index, item) {
//                 // 이미 버튼이 추가된 상태에서 중복 추가를 막기 위해 확인
//                 const existingButton = medicationList.querySelector(`[value="${item.value}"]`);
//                 if (!existingButton) {
//                     addMedicationButton(item.label);
//                 }
//             });
//         }
//     });
// }

// // ajax 요청을 보내는 함수
// function updateNutritionChoices(newNutrition) {
//     $.ajax({
//         url: "/add_nutrition/",
//         method: "POST",
//         data: { new_nutrition: newNutrition, csrfmiddlewaretoken: csrfToken },
//         dataType: "json",
//         success: function (data) {
//             // 업데이트된 선택지를 화면에 반영
//             $.each(data.nutrition_list, function (index, item) {
//                 // 이미 버튼이 추가된 상태에서 중복 추가를 막기 위해 확인
//                 const existingButton = nutritionList.querySelector(`[value="${item.value}"]`);
//                 if (!existingButton) {
//                     addNutritionButton(item.label);
//                 }
//             });
//         }
//     });
// }









//
document.addEventListener("click", async function (event) {
    const medicationInput = document.getElementById("medication-input");
    const medicationList = document.getElementById("medication-list");

    if (!medicationInput.contains(event.target) && !medicationList.contains(event.target)) {
        const newMedication = medicationInput.value.trim();
        if (newMedication !== "") {
            // 약 추가 AJAX 요청
            try {
                const response = await fetch('/add-medication/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': csrfToken // 실제 CSRF 토큰 값으로 교체
                    },
                    body: `new_medication=${encodeURIComponent(newMedication)}`
                });
                const data = await response.json();
                console.log(data);

                // 약 버튼 추가 및 스타일 변경
                const medicationItem = document.createElement("button");
                medicationItem.textContent = newMedication;
                medicationItem.type = "button";
                medicationItem.className = "selected-drug-button";
                userChoiceContents.appendChild(medicationItem);

                medicationInput.value = "";
                medicationList.style.maxHeight = medicationList.scrollHeight + "px";
            } catch (error) {
                console.error('에러:', error);
            }
        }
    }
});

// 영양제 선택 로직도 비슷하게 구현



document.addEventListener("click", function (event) {
    const nutriInput = document.getElementById("nutri-input");
    const nutriList = document.querySelector(".user-nutri-content");

    if (!nutriInput.contains(event.target) && !nutriList.contains(event.target)) {
        const newNutrition = nutriInput.value.trim();
        if (newNutrition !== "") {
            const nutriItem = document.createElement("button");
            nutriItem.textContent = newNutrition;
            nutriItem.type = "button";

            const vitaminEButton = document.querySelector(".nutri-14");
            if (vitaminEButton.nextSibling && vitaminEButton.nextSibling.tagName === "BUTTON") {
                vitaminEButton.parentNode.insertBefore(nutriItem, vitaminEButton.nextSibling);
            } else {
                vitaminEButton.parentNode.appendChild(nutriItem);
            }

            nutriInput.value = "";

             // 확장을 위한 코드 추가
             nutriList.style.maxHeight = nutriList.scrollHeight + "px";
        }
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const userChoiceContents = document.querySelector(".user-choice-contents");
    const drugButtons = document.querySelectorAll(".user-drug-content button");
    const nutriButtons = document.querySelectorAll(".user-nutri-content button");
  
    drugButtons.forEach(function (button) {
      button.addEventListener("click", function () {
        const selectedDrug = button.textContent;
        const selectedChoice = document.createElement("button"); // 버튼 태그로 변경
        selectedChoice.textContent = `${selectedDrug}`;
        selectedChoice.className = "selected-drug-button"; // 클래스 추가
        userChoiceContents.appendChild(selectedChoice);
      });
    });
  
    nutriButtons.forEach(function (button) {
      button.addEventListener("click", function () {
        const selectedNutri = button.textContent;
        const selectedChoice = document.createElement("button"); 
        selectedChoice.textContent = `${selectedNutri}`;
        selectedChoice.className = "selected-drug-button"; // 클래스 추가
        userChoiceContents.appendChild(selectedChoice);
      });
    });
  });
  
  // 사용자가 직접 복용하는 약 추가
function updateMedicationChoices(newMedication) {
    $.ajax({
        url: "accounts/add_medication/",
        method: "POST",
        data: { new_medication: newMedication },
        dataType: "json",
        success: function (data) {
            // 업데이트된 선택지를 화면에 반영
            var medicationList = $("#medication-list");  // 약 선택 목록 id
            medicationList.empty();  // 기존 목록 비우기
            $.each(data.medication_list, function (index, item) {
                var button = $('<button>', {
                    type: "button",
                    name: "medication_choice",
                    value: item.value,
                    text: item.label
                });
                medicationList.append(button);
            });
        }
    });
}

// 사용자가 직접 복용하는 영양제 추가
function updateNutritionChoices(newNutrition) {
    $.ajax({
        url: "/accounts/add_nutrition/",
        method: "POST",
        data: { new_nutrition: newNutrition },
        dataType: "json",
        success: function (data) {
            // 업데이트된 선택지를 화면에 반영
            var nutritionList = $("#nutrition-list");  // 영양제 선택 목록 id
            nutritionList.empty();  // 기존 목록 비우기
            $.each(data.nutrition_list, function (index, item) {
                var button = $('<button>', {
                    type: "button",
                    name: "nutrition_choice",
                    value: item.value,
                    text: item.label
                });
                nutritionList.append(button);
            });
        }
    });
}