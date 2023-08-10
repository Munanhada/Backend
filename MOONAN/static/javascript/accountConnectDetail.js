const maleButton = document.getElementById('male-button');
const femaleButton = document.getElementById('female-button');
const resultDiv = document.getElementById('result');

function handleButtonClick(gender) {
    maleButton.classList.remove('active', 'disabled');
    femaleButton.classList.remove('active', 'disabled');
    
    if (gender === 'male') {
        maleButton.classList.add('active');
        resultDiv.textContent = '남자';
    } else if (gender === 'female') {
        femaleButton.classList.add('active');
        resultDiv.textContent = '여자';
    }
}

maleButton.addEventListener('click', () => {
    if (!maleButton.classList.contains('active')) {
        handleButtonClick('male');
    }
});

femaleButton.addEventListener('click', () => {
    if (!femaleButton.classList.contains('active')) {
        handleButtonClick('female');
    }
});
