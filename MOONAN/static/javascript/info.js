// 텍스트 입력 외부 영역 클릭을 감지하는 이벤트 핸들러
document.addEventListener("click", function (event) {
    const medicationInput = document.getElementById("medication-input");
    const medicationList = document.getElementById("medication-list");

    // 텍스트 입력 영역을 제외한 영역을 클릭했을 때만 실행
    if (!medicationInput.contains(event.target) && !medicationList.contains(event.target)) {
        const medicationName = medicationInput.value.trim();
        updateMedicationChoices(medicationName);
        medicationInput.value = "";
    }
});

document.addEventListener("click", function (event) {
    const nutritionInput = document.getElementById("nutrition-input");
    const nutritionList = document.getElementById("nutrition-list");

    if (!nutritionInput.contains(event.target) && !nutritionList.contains(event.target)) {
        const nutritionName = nutritionInput.value.trim();
        updateNutritionChoices(nutritionName);
        nutritionInput.value = "";
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
            var medicationSelect = $("#medication-list");  // 약 선택 필드 id
    
            // 기존 버튼들을 선택
            var existingButtons = medicationSelect.find("button[name='medication']");
    
            // 마지막 버튼을 선택
            var lastButton = existingButtons.last();
    
            // 버튼을 생성하고 추가
            var button = $("<button>", {
                class: "your-button-class", // 버튼에 적절한 클래스명 지정
                text: newMedication, // 받아온 영양제 이름을 버튼 텍스트로 사용
                click: function () {
                    // 버튼이 클릭되었을 때 실행할 동작을 여기에 작성
                }
            });
    
            // 마지막 버튼 뒤에 생성된 버튼을 추가
            lastButton.after(button);
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
            $.each(data.nutrition_list, function (index, item) {
                var button = $("<button>", {
                    class: "your-button-class", // 버튼에 적절한 클래스명 지정
                    text: item.label, // 받아온 옵션 레이블을 버튼 텍스트로 사용
                    click: function () {
                        // 버튼이 클릭되었을 때 실행할 동작을 여기에 작성
                    }
                });
            });
            
            var nutritionSelect = $("#nutrition-list");  // 영양제 선택 필드 id
    
            // 기존 버튼들을 선택
            var existingButtons = nutritionSelect.find("button[name='nutrition']");
    
            // 마지막 버튼을 선택
            var lastButton = existingButtons.last();
    
            // 버튼을 생성하고 추가
            var button = $("<button>", {
                class: "your-button-class", // 버튼에 적절한 클래스명 지정
                text: newNutrition, // 받아온 영양제 이름을 버튼 텍스트로 사용
                click: function () {
                    // 버튼이 클릭되었을 때 실행할 동작을 여기에 작성
                }
            });
    
            // 마지막 버튼 뒤에 생성된 버튼을 추가
            lastButton.after(button);
        }
    });
}






// 사용자가 직접 복용하는 약 추가
function updateMedicationChoices(newMedication) {
    $.ajax({
        url: "/add_medication/",
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
        url: "/add_nutrition/",
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