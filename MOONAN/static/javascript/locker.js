
// 년, 월 선택 
const monthSelect = document.getElementById('monthSelect');
const currentDate = new Date();

for (let i = 5; i >= 0; i--) {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth() - i;
    
    if (month < 0) {
        month += 12;
        year -= 1;
    }
    
    const formattedMonth = (month + 1).toString().padStart(2, '0');
    const optionValue = `${year}-${formattedMonth}`;
    const optionText = `${year}년 ${formattedMonth}월`;
    
    const option = document.createElement('option');
    option.value = optionValue;
    option.textContent = optionText;
    
    monthSelect.appendChild(option);
}

// 이번달 기본 선택
const currentYear = currentDate.getFullYear();
const currentMonth = (currentDate.getMonth() + 1).toString().padStart(2, '0');
const currentOptionValue = `${currentYear}-${currentMonth}`;

monthSelect.value = currentOptionValue;

// 선택한 month 달력에 출력

let date = new Date(); // 현재 날짜 가져오는 Date 객체 생성

const viewYear = date.getFullYear(); // 현재 년도 가져오기
const viewMonth = (date.getMonth() + 1).toString().padStart(2, '0'); // 현재 월 가져오기, 2자리로 변환
    
const prevLast = new Date(viewYear, viewMonth - 1, 0); // 이전 달의 마지막 날짜 가져오기
const thisLast = new Date(viewYear, viewMonth, 0); // 현재 달의 마지막 날짜 가져오기

const PLDate = prevLast.getDate(); // 이전 달 마지막 날짜
const PLDay = prevLast.getDay(); // 이전 달 마지막 날짜의 요일

const TLDate = thisLast.getDate(); // 현재 달 마지막 날짜
const TLDay = thisLast.getDay(); // 현재 달 마지막 날짜의 요일

const thisDates = [...Array(TLDate + 1).keys()].slice(1);
const dates = thisDates

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

            // 현재 달의 날짜 생성
            for (let i = 1; i <= daysInMonth; i++) {
                const dateElement = document.createElement('div');
                dateElement.classList.add('date');
                dateElement.textContent = i;

                // 이미지 경로 설정
                const imagePath = `../../static/image/expression/empty.svg`;  // 이미지 경로에 맞게 수정

                const image = new Image();
                image.src = imagePath;
                dateElement.appendChild(image);

                datesContainer.appendChild(dateElement);
            }
        }

        // 선택한 달의 날짜 업데이트
        monthSelect.addEventListener('change', function () {
            const selectedDate = new Date(monthSelect.value + '-01');
            updateCalendar(selectedDate);
        });

        // 초기에 현재 달의 날짜 표시
        const currentDate = new Date();
        monthSelect.value = `${currentDate.getFullYear()}-${('0' + (currentDate.getMonth() + 1)).slice(-2)}`;
        updateCalendar(currentDate);
    })







//할 일
const expression = 0;

const renderCalendar = () => {
    const viewYear = date.getFullYear(); // 현재 년도 가져오기
    const viewMonth = (date.getMonth() + 1).toString().padStart(2, '0'); // 현재 월 가져오기, 2자리로 변환
    


};