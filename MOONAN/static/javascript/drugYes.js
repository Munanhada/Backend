const medications = [];
const nutritions = [];

document.addEventListener("DOMContentLoaded", function () {
    const userChoiceContents = document.querySelector(".user-choice-contents");
    const medicationInput = document.getElementById("medication-input");
    const medicationList = document.getElementById("medication-list");
    const nutritionInput = document.getElementById("nutri-input");
    const nutritionList = document.getElementById("nutrition-list");

    // 기존에 선택한 버튼들을 저장하는 배열
    const selectedButtons = [];

    function addMedicationButton(medicationName) {
        const medicationButton = document.createElement("button");
        medicationButton.type = "button";
        medicationButton.name = "medication_choice";
        medicationButton.value = medicationName;
        medicationButton.textContent = medicationName;
        const lastButton = medicationList.querySelector("button:last-of-type");
        medicationList.insertBefore(medicationButton, lastButton.nextSibling);
        medicationInput.value = "";

        // 생성한 버튼에 클릭 이벤트 리스너 추가
        medicationButton.addEventListener("click", function () {
            const selectedDrug = medicationName;
            toggleSelection(medicationButton, selectedDrug);
            // medications 리스트에 추가
            medications.push(medicationName);
            console.log("medications:", medications);
        });
    }

    function addNutritionButton(nutritionName) {
        const nutritionButton = document.createElement("button");
        nutritionButton.type = "button";
        nutritionButton.name = "nutrition_choice";
        nutritionButton.value = nutritionName;
        nutritionButton.textContent = nutritionName;
        const lastButton = nutritionList.querySelector("button:last-of-type");
        nutritionList.insertBefore(nutritionButton, lastButton.nextSibling);
        nutritionInput.value = "";

        // 생성한 버튼에 클릭 이벤트 리스너 추가
        nutritionButton.addEventListener("click", function () {
            const selectedNutri = nutritionName;
            toggleSelection(nutritionButton, selectedNutri);
            // nutritions 리스트에 추가
            nutritions.push(nutritionName);
            console.log("nutritions:", nutritions);
        });
    }

    // 외부 영역 클릭 시
    document.addEventListener("click", function (event) {
        // "복용중인 약" 입력 외부 영역 클릭 시
        if (!medicationInput.contains(event.target) && !medicationList.contains(event.target)) {
            const newMedication = medicationInput.value.trim();
            if (newMedication !== "") {
                addMedicationButton(newMedication);
                addMedication(newMedication);
            }
        }

        // "복용중인 영양제" 입력 외부 영역 클릭 시
        if (!nutritionInput.contains(event.target) && !nutritionList.contains(event.target)) {
            const newNutrition = nutritionInput.value.trim();
            if (newNutrition !== "") {
                addNutritionButton(newNutrition);
                addNutrition(newNutrition);
            }
        }
    });

    function toggleSelection(button, value) {
        const isAlreadySelected = selectedButtons.includes(value);
        if (isAlreadySelected) {
            const index = selectedButtons.indexOf(value);
            if (index > -1) {
                selectedButtons.splice(index, 1);
            }
            button.classList.remove("selected");
        } else {
            selectedButtons.push(value);
            button.classList.add("selected");
        }
        updateSelectedChoices();
    }

    // 선택한 버튼 목록을 업데이트하는 함수
    function updateSelectedChoices() {
        userChoiceContents.innerHTML = ""; // 기존 내용 삭제

        // 선택한 버튼들을 출력
        selectedButtons.forEach(function (selectedItem) {
            const selectedChoice = document.createElement("button");
            selectedChoice.textContent = selectedItem;
            selectedChoice.className = "selected-drug-button";
            userChoiceContents.appendChild(selectedChoice);
        });
    }

    // "복용중인 약" 버튼들에 대한 클릭 이벤트 리스너 등록
    const drugButtons = document.querySelectorAll(".user-drug-content button");
    drugButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const selectedDrug = button.textContent;
            toggleSelection(button, selectedDrug);
        });
    });

    // "복용중인 영양제" 버튼들에 대한 클릭 이벤트 리스너 등록
    const nutriButtons = document.querySelectorAll(".user-nutri-content button");
    nutriButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const selectedNutri = button.textContent;
            toggleSelection(button, selectedNutri);
        });
    });
});


// 사용자가 직접 복용하는 약 추가
function addMedication(newMedication) {
    // CSRF 토큰 가져오기
    const csrfToken = getCookie("csrftoken");

    $.ajax({
        url: "/accounts/add_medication/",
        method: "POST",
        data: { new_medication: newMedication },
        headers: {
            "X-CSRFToken": csrfToken  // CSRF 토큰을 요청 헤더에 추가
        },
        dataType: "json",
        success: function (data) {
            console.log("서버 응답 데이터:", data); // 서버 응답 정보 출력
            // 선택지 목록 업데이트 등의 처리
        },
        error: function (xhr, textStatus, errorThrown) {
            console.error("에러 발생:", textStatus, errorThrown); // 에러 정보 출력
        }
    });
}

// 사용자가 직접 복용하는 영양제 추가
function addNutrition(newNutrition) {
    // CSRF 토큰 가져오기
    const csrfToken = getCookie("csrftoken");

    $.ajax({
        url: "/accounts/add_nutrition/",
        method: "POST",
        data: { new_nutrition: newNutrition },
        headers: {
            "X-CSRFToken": csrfToken  // CSRF 토큰을 요청 헤더에 추가
        },
        dataType: "json",
        success: function (data) {
            console.log("서버 응답 데이터:", data); // 서버 응답 정보 출력
        },
        error: function (xhr, textStatus, errorThrown) {
            console.error("에러 발생:", textStatus, errorThrown); // 에러 정보 출력
        }
    });
}

// 쿠키에서 CSRF 토큰 가져오기 함수
function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length === 2) {
        return parts.pop().split(";").shift();
    }
}

// 데이터를 업데이트하는 함수
function updateData() {
    $.get("/get_updated_data/", function(data) {
        // 서버에서 받은 데이터를 이용하여 화면 업데이트
        $(".user-drug-list").empty(); // 기존 버튼들 제거
        console.log(data.user_medication)
        console.log(data.user_nutrition)

        // 약 데이터 업데이트
        data.user_medications.forEach(function(um) {
            var button = $('<button type="button" class="user-medication"></button>');
            button.append($('<p class="detail-drug"></p>').text(um.medication));
            $(".user-drug-list").append(button);
        });

        // 영양제 데이터 업데이트
        data.user_nutritions.forEach(function(un) {
            var button = $('<button type="button" class="user-nutrition"></button>');
            button.append($('<p class="detail-drug"></p>').text(un.nutrition));
            $(".user-drug-list").append(button);
        });
    });
}

$(document).ready(function() {
    updateData();
    setInterval(updateData, 5000);
    $(".user-drug-button").click(function() {
        const medication = $(this).data("medication");
        if (!medications.includes(medication)) {
            medications.push(medication);
            $(this).addClass("selected");
            $(this).toggleClass("selected-button");
        } else {
            const index = medications.indexOf(medication);
            if (index > -1) {
                medications.splice(index, 1);
            }
            $(this).removeClass("selected");
        }
        console.log("medications:", medications);
    });

    $(".user-nutri-button").click(function() {
        const nutrition = $(this).data("nutrition");
        if (!nutritions.includes(nutrition)) {
            nutritions.push(nutrition);
            $(this).addClass("selected");
        } else {
            const index = nutritions.indexOf(nutrition);
            if (index > -1) {
                nutritions.splice(index, 1);
            }
            $(this).removeClass("selected");
        }
        console.log("nutritions:", nutritions);
    });

    $(".next-step").click(function() {
        // 선택 완료 버튼 클릭 시 이벤트 핸들러
        $("form").submit();
    });

    $("form").on("submit", function(event) {
        let med_or_nutr_status = $("input[name='med_or_nutr_status']:checked").val() === "True" ? "True" : "False";

        console.log("med_or_nutr_status:", med_or_nutr_status);
        console.log("medications:", medications);
        console.log("nutritions:", nutritions);

        // 폼 데이터를 제출하고 서버 응답 처리
        $.post("/accounts/med_nutr_data/", {
            med_or_nutr_status: med_or_nutr_status,
            medication: medications,
            nutrition: nutritions,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        })
        .done(function(data) {
            // 서버 응답 처리 코드
            console.log("Server Response:", data); // 서버 응답 출력
            // 가져온 데이터를 사용하여 화면 업데이트
            window.location.href = "/home"; // home으로 리디렉션
        })
        .fail(function(error) {
            // 실패 시 처리 코드
            console.error("Error:", error);
        });
    });
});