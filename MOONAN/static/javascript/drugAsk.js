document.addEventListener('DOMContentLoaded', function () {
    const drugYesRadio = document.getElementById('drug-yes');
    const drugNoRadio = document.getElementById('drug-no');
    const drugYesLabel = document.querySelector('.drug-ask-box-yes');
    const drugNoLabel = document.querySelector('.drug-ask-box-no');
    const drugYesSpan = document.querySelector('.drug-ask-box-yes span');
    const drugNoSpan = document.querySelector('.drug-ask-box-no span');
    const drugYesEllipseImage = drugYesLabel.querySelector('img[alt="원형 이미지"]');
    const drugYesDoneImage = drugYesLabel.querySelector('img[alt="체크 이미지"]');
    const drugNoEllipseImage = drugNoLabel.querySelector('img[alt="원형 이미지"]');
    const drugNoDoneImage = drugNoLabel.querySelector('img[alt="체크 이미지"]');
    const progressElement = document.getElementById('progress');
    const progressCircleImage = document.querySelector('.progress-circle');
    const iconWrapper = document.querySelector('.icon-wrapper');
    const progressDropImage = document.querySelector('.progress-drop');
    const originalDrugYesEllipseImagePath = drugYesEllipseImage.src;
    const originalDrugYesDoneImagePath = drugYesDoneImage.src;
    const originalDrugNoEllipseImagePath = drugNoEllipseImage.src;
    const originalDrugNoDoneImagePath = drugNoDoneImage.src;
    const originalProgressValue = progressElement.value;

    drugYesRadio.addEventListener('change', function () {
        if (drugYesRadio.checked) {
            drugYesLabel.style.backgroundColor = '#FF003A';
            drugNoLabel.style.backgroundColor = '';
            drugYesSpan.style.color = 'white';
            drugNoSpan.style.color = '';
            drugYesEllipseImage.src = '/static/image/Ellipse 82.svg';
            drugYesDoneImage.src = '/static/image/Done red.svg';
            drugNoEllipseImage.src = originalDrugNoEllipseImagePath;
            drugNoDoneImage.src = originalDrugNoDoneImagePath;
            progressElement.value = 75;
            progressCircleImage.style.left = '75%';
            iconWrapper.style.left = '75%';
            iconWrapper.style.bottom = '200%';
            progressDropImage.style.left = '75%';
        } else {
            drugYesLabel.style.backgroundColor = '';
            drugYesSpan.style.color = '';
            drugYesEllipseImage.src = originalDrugYesEllipseImagePath;
            drugYesDoneImage.src = originalDrugYesDoneImagePath;
            progressElement.value = originalProgressValue;
            progressCircleImage.style.left = '100%';
            iconWrapper.style.left = '100%';
            iconWrapper.style.bottom = '200%';
            progressDropImage.style.left = '100%';
        }
    });

    drugNoRadio.addEventListener('change', function () {
        if (drugNoRadio.checked) {
            drugYesLabel.style.backgroundColor = '';
            drugNoLabel.style.backgroundColor = '#FF003A';
            drugYesSpan.style.color = '';
            drugNoSpan.style.color = 'white';
            drugYesEllipseImage.src = originalDrugYesEllipseImagePath;
            drugYesDoneImage.src = originalDrugYesDoneImagePath;
            drugNoEllipseImage.src = '/static/image/Ellipse 82.svg';
            drugNoDoneImage.src = '/static/image/Done red.svg';
            progressElement.value = originalProgressValue;
            progressCircleImage.style.left = '100%';
            iconWrapper.style.left = '100%';
            iconWrapper.style.bottom = '200%';
            progressDropImage.style.left = '100%';
        } else {
            drugNoLabel.style.backgroundColor = '';
            drugNoSpan.style.color = '';
            drugNoEllipseImage.src = originalDrugNoEllipseImagePath;
            drugNoDoneImage.src = originalDrugNoDoneImagePath;
            progressElement.value = originalProgressValue;
            progressCircleImage.style.left = '100%';
            iconWrapper.style.left = '100%';
            iconWrapper.style.bottom = '200%';
            progressDropImage.style.left = '100%';
        }
    });

    drugYesLabel.addEventListener('click', function () {
        drugNoLabel.style.backgroundColor = '';
        drugNoSpan.style.color = '';
        drugNoEllipseImage.src = originalDrugNoEllipseImagePath;
        drugNoDoneImage.src = originalDrugNoDoneImagePath;
        progressElement.value = 75;
        progressCircleImage.style.left = '75%';
        iconWrapper.style.left = '100%';
        iconWrapper.style.bottom = '200%';
        progressDropImage.style.left = '75%';
    });

    drugNoLabel.addEventListener('click', function () {
        drugYesLabel.style.backgroundColor = '';
        drugYesSpan.style.color = '';
        drugYesEllipseImage.src = originalDrugYesEllipseImagePath;
        drugYesDoneImage.src = originalDrugYesDoneImagePath;
        progressElement.value = originalProgressValue;
        progressCircleImage.style.left = '100%';
        iconWrapper.style.left = '100%';
        iconWrapper.style.bottom = '200%';
        progressDropImage.style.left = '100%';
    });
});
