// DOM이 로드된 후에 스크립트 실행
document.addEventListener('DOMContentLoaded', function () {
    const monthSelect = document.getElementById('monthSelect');
    const datesContainer = document.querySelector('.dates');
    
    function updateDates(selectedDate) {
        datesContainer.innerHTML = ''; // 기존 내용 비우기
        
        const selectedYear = selectedDate.getFullYear();
        const selectedMonth = selectedDate.getMonth();
        const daysInMonth = new Date(selectedYear, selectedMonth + 1, 0).getDate();
        
        for (let i = 1; i <= daysInMonth; i++) {
            const date = new Date(selectedYear, selectedMonth, i);
            const dayOfWeek = date.getDay();
            
            const dateElement = document.createElement('div');
            dateElement.classList.add('date');
            dateElement.textContent = i;
            
            datesContainer.appendChild(dateElement);
        }
    }
    
    // 선택한 달의 날짜 업데이트
    monthSelect.addEventListener('change', function () {
        const selectedValue = monthSelect.value;
        const [selectedYear, selectedMonth] = selectedValue.split('-');
        const selectedDate = new Date(selectedYear, selectedMonth - 1);
        
        updateDates(selectedDate);
    });
    
    // 초기에 현재 달의 날짜 표시
    const currentDate = new Date();
    monthSelect.value = `${currentDate.getFullYear()}-${currentDate.getMonth() + 1}`;
    updateDates(currentDate);
});