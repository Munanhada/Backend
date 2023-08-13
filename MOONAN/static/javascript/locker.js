
// 년, 월 선택 
const monthSelect = document.getElementById('monthSelect');
const currentDate = new Date();
const currentYear = currentDate.getFullYear();
const currentMonth = (currentDate.getMonth() + 1).toString().padStart(2, '0');
const currentOptionValue = `${currentYear}-${currentMonth}`;

for (let i = 5; i >= 0; i--) {
    const year = currentYear;
    let month = currentMonth - i;
    
    if (month < 1) {
        month += 12;
        year -= 1;
    }
    
    const formattedMonth = month.toString().padStart(2, '0');
    const optionValue = `${year}-${formattedMonth}`;
    const optionText = `${year}년 ${formattedMonth}월`;
    
    const option = document.createElement('option');
    option.value = optionValue;
    option.textContent = optionText;
    
    monthSelect.appendChild(option);
}

// 이번달 기본 선택
monthSelect.value = currentOptionValue;


//출력 ----------------------------------
// DOM이 로드된 후에 스크립트 실행
document.addEventListener('DOMContentLoaded', function () {
    const monthSelect = document.getElementById('monthSelect');
    const daysContainer = document.querySelector('.days');
    const datesContainer = document.querySelector('.dates');
    const dayNames = ['일', '월', '화', '수', '목', '금', '토'];


    function updateCalendar(selectedDate) {
        daysContainer.innerHTML = ''; // 요일 업데이트
        datesContainer.innerHTML = ''; // 날짜 업데이트

        const currentMonth = selectedDate.getMonth();
        const currentYear = selectedDate.getFullYear();
        const firstDayOfMonth = new Date(currentYear, currentMonth, 1);
        const lastDayOfMonth = new Date(currentYear, currentMonth + 1, 0);
        const daysInMonth = lastDayOfMonth.getDate();

        // 요일명 생성
        for (const dayName of dayNames) {
            const dayElement = document.createElement('div');
            dayElement.classList.add('day');
            dayElement.textContent = dayName;
            daysContainer.appendChild(dayElement);
        }

        // 이전 달의 마지막 날짜
        const lastDayOfPrevMonth = new Date(currentYear, currentMonth, 0).getDate();

        // 이전 달의 빈 칸 생성
        for (let i = firstDayOfMonth.getDay(); i > 0; i--) {
            const emptyElement = document.createElement('div');
            emptyElement.classList.add('empty');
            datesContainer.appendChild(emptyElement);
        }

        const selectedMonth = selectedDate.getMonth() + 1;
        const selectedYear = selectedDate.getFullYear();

        // 현재 달의 날짜 생성
        for (let i = 1; i <= daysInMonth; i++) {
            const dateBorderElement = document.createElement('div');
            dateBorderElement.classList.add('date-border');
            
            const dateElement = document.createElement('div');
            dateElement.classList.add('date');

            const dayNumberElement = document.createElement('div');
            dayNumberElement.classList.add('day-number');

            // 여기서 선택한 날짜인 경우 클래스를 추가
            if (i === currentDate.getDate() && currentMonth === selectedMonth && currentYear === selectedYear) {
                dateBorderElement.classList.add('selected-date');
            }

            dayNumberElement.textContent = i;
            dateElement.appendChild(dayNumberElement);
            
            const image = new Image();
            const imagePath = `../../static/image/expression/empty.svg`;
            image.src = imagePath;
            
            dateElement.appendChild(image);
            dateBorderElement.appendChild(dateElement);

            datesContainer.appendChild(dateBorderElement);
        }


    }

    // 선택한 달의 날짜 업데이트
    monthSelect.addEventListener('change', function () {
        const selectedDate = new Date(monthSelect.value + '-01');
        updateCalendar(selectedDate);
    });

    // 초기에 현재 달의 날짜 표시
    monthSelect.value = `${currentYear}-${('0' + (currentDate.getMonth() + 1)).slice(-2)}`;
    updateCalendar(currentDate);


    // 선택한 달의 날짜 업데이트
    monthSelect.addEventListener('change', function () {
        const selectedDate = new Date(monthSelect.value + '-01');
        updateCalendar(selectedDate);
    });

    // 날짜 클릭 이벤트 처리
    datesContainer.addEventListener('click', function (event) {
        const clickedDateElement = event.target.closest('.date'); // .date 요소를 찾음
    
        if (clickedDateElement) {
            const clickedDate = clickedDateElement.querySelector('div').textContent;
            const selectedYear = new Date(monthSelect.value + '-01').getFullYear();
            const selectedMonth = new Date(monthSelect.value + '-01').getMonth() + 1;
    
            // 기존에 선택한 날짜의 클래스를 삭제
            const prevSelected = datesContainer.querySelector('.selected-date');
            if (prevSelected) {
                prevSelected.classList.remove('selected-date');
            }

            // 선택한 날짜에 클래스를 추가하여 스타일 적용
            event.target.classList.add('selected-date');

            const recordDayElement = document.querySelector('.recordday p');
            recordDayElement.textContent = `${selectedYear}년 ${selectedMonth}월 ${clickedDate}일의 문안기록`;
    
            // 선택한 날짜의 기록 정보를 가져와서 .selectedrecord 에 추가하는 로직 추가 가능
        }
    });

    // 초기에 현재 달의 날짜 표시
    monthSelect.value = `${currentYear}-${('0' + (currentMonth + 1)).slice(-2)}`;
    updateCalendar(currentDate);
});







//할 일
const expression = 0;

const renderCalendar = () => {
    const viewYear = date.getFullYear(); // 현재 년도 가져오기
    const viewMonth = (date.getMonth() + 1).toString().padStart(2, '0'); // 현재 월 가져오기, 2자리로 변환
    


};