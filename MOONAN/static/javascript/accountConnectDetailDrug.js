var selectedButton = null;

function toggleImg(buttonId) {
    if (selectedButton !== buttonId) {
        if (selectedButton !== null) {
            resetButton(selectedButton);
        }
        updateButton(buttonId);
        selectedButton = buttonId;
    } else {
        resetButton(buttonId);
        selectedButton = null;
    }
}

function updateButton(buttonId) {
    var iconCircle = document.getElementById("icon-circle-" + buttonId.split("-")[0]);
    var iconDone = document.getElementById("icon-done-" + buttonId.split("-")[0]);
    iconCircle.src = "/static/image/Ellipse 82.svg";
    iconDone.src = "/static/image/Done red.svg";
}

function resetButton(buttonId) {
    var iconCircle = document.getElementById("icon-circle-" + buttonId.split("-")[0]);
    var iconDone = document.getElementById("icon-done-" + buttonId.split("-")[0]);
    iconCircle.src = "/static/image/Ellipse 82 gray.svg";
    iconDone.src = "/static/image/Done.svg";
}