document.addEventListener("DOMContentLoaded", function () {
    const medicationInput = document.getElementById("medication-input");
    const medicationList = document.getElementById("medication-list");

    const nutritionInput = document.getElementById("nutrition-input");
    const nutritionList = document.getElementById("nutrition-list");

    function addMedicationButton(medicationName) {
        const medicationButton = document.createElement("button");
        medicationButton.type = "button";
        medicationButton.name = "medication_choice";
        medicationButton.value = medicationName;
        medicationButton.textContent = medicationName;
        medicationList.appendChild(medicationButton);
        medicationInput.value = "";
    }

    function addNutritionButton(nutritionName) {
        const nutritionButton = document.createElement("button");
        nutritionButton.type = "button";
        nutritionButton.name = "nutrition_choice";
        nutritionButton.value = nutritionName;
        nutritionButton.textContent = nutritionName;
        nutritionList.appendChild(nutritionButton); 
        nutritionInput.value = "";
    }

    // "복용중인 약" 입력 외부 영역 클릭 시
    document.addEventListener("click", function (event) {
        if (!medicationInput.contains(event.target) && !medicationList.contains(event.target)) {
            const newMedication = medicationInput.value.trim();
            if (newMedication !== "") {
                addMedicationButton(newMedication);
            }
        }
    });

    // "복용중인 영양제" 입력 외부 영역 클릭 시
    document.addEventListener("click", function (event) {
        if (!nutritionInput.contains(event.target) && !nutritionList.contains(event.target)) {
            const newNutrition = nutritionInput.value.trim();
            if (newNutrition !== "") {
                addNutritionButton(newNutrition);
            }
        }
    });
});

// ajax 요청을 보내는 함수
function updateMedicationChoices(newMedication) {
    $.ajax({
        url: "/add_medication/",
        method: "POST",
        data: { new_medication: newMedication, csrfmiddlewaretoken: csrfToken },
        dataType: "json",
        success: function (data) {
            // 업데이트된 선택지를 화면에 반영
            $.each(data.medication_list, function (index, item) {
                // 이미 버튼이 추가된 상태에서 중복 추가를 막기 위해 확인
                const existingButton = medicationList.querySelector(`[value="${item.value}"]`);
                if (!existingButton) {
                    addMedicationButton(item.label);
                }
            });
        }
    });
}

// ajax 요청을 보내는 함수
function updateNutritionChoices(newNutrition) {
    $.ajax({
        url: "/add_nutrition/",
        method: "POST",
        data: { new_nutrition: newNutrition, csrfmiddlewaretoken: csrfToken },
        dataType: "json",
        success: function (data) {
            // 업데이트된 선택지를 화면에 반영
            $.each(data.nutrition_list, function (index, item) {
                // 이미 버튼이 추가된 상태에서 중복 추가를 막기 위해 확인
                const existingButton = nutritionList.querySelector(`[value="${item.value}"]`);
                if (!existingButton) {
                    addNutritionButton(item.label);
                }
            });
        }
    });
}
