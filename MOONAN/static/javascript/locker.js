
// 년, 월 선택 
const monthSelect = document.getElementById('monthSelect');
const currentDate = new Date();
const currentYear = currentDate.getFullYear();
const currentMonth = (currentDate.getMonth() + 1).toString().padStart(2, '0');
const currentOptionValue = `${currentYear}년 ${currentMonth}월`;

// 이번 달 기준으로 5개월 전만 선택가능
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
