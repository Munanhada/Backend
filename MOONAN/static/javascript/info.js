// 텍스트 입력 외부 영역 클릭을 감지하는 이벤트 핸들러
document.addEventListener("click", function (event) {
    const medicationInput = document.getElementById("medicationInput");
    const medicationList = document.getElementById("medicationList");

    // 텍스트 입력 영역을 제외한 영역을 클릭했을 때만 실행
    if (!medicationInput.contains(event.target) && !medicationList.contains(event.target)) {
        const medicationName = medicationInput.value;
        saveMedication(medicationName);
    }
});

document.addEventListener("click", function (event) {
    const nutritionInput = document.getElementById("nutritionInput");
    const nutritionList = document.getElementById("nutritionList");

    if (!nutritionInput.contains(event.target) && !nutritionList.contains(event.target)) {
        const nutritionName = nutritionInput.value;
        saveMedication(nutritionName);
    }
});

// ajax 요청을 보내고 선택지 목록을 업데이트하는 함수
function updateMedicationChoices(newMedication) {
    $.ajax({
        url: "/add_medication/",
        method: "POST",
        data: { new_medication: newMedication },
        dataType: "json",
        success: function (data) {
            // 업데이트된 선택지를 화면에 반영
            var medicationSelect = $("#medication-select");  // 약 선택 필드 id
            medicationSelect.empty();  // 기존 선택지 비우기
            $.each(data.medication_list, function (index, item) {
                medicationSelect.append($('<option>', {
                    value: item.value,
                    text: item.label
                }));
            });
        }
    });
}


// ajax 요청을 보내고 선택지 목록을 업데이트하는 함수
function updateNutritionChoices(newNutrition) {
    $.ajax({
        url: "/add_nutrition/",
        method: "POST",
        data: { new_nutrition: newNutrition },
        dataType: "json",
        success: function (data) {
            // 업데이트된 선택지를 화면에 반영
            var nutritionSelect = $("#nutrition-select");  // 영양제 선택 필드 id
            nutritionSelect.empty();  // 기존 선택지 비우기
            $.each(data.nutrition_list, function (index, item) {
                nutritionSelect.append($('<option>', {
                    value: item.value,
                    text: item.label
                }));
            });
        }
    });
}
