let faze1val = 42;
let faze2val = 105;
let uhelvalX = 0;
let uhelvalY = 0;
let rychlostval = 50;
let rotateX = true;
let rotateY = true;

let id;

let posunX = 0;
let posunY = 0;

let canvas = document.getElementById("myCanvas");
let contex = canvas.getContext("2d");

let inputBoxFaze1 = document.querySelector("#faze1");
let inputBoxFaze2 = document.querySelector("#faze2");
let inputBoxRychlost = document.querySelector("#rychlost");


if (inputBoxFaze1 !== null) {
    inputBoxFaze1.addEventListener("input", function () {
        faze1val = this.value;
        drawImage(faze1val, faze2val, uhelvalX, uhelvalY);
    });
}

if (inputBoxFaze2 !== null) {
    inputBoxFaze2.addEventListener("input", function () {
        faze2val = this.value;
        drawImage(faze1val, faze2val, uhelvalX, uhelvalY);
    });
}

if (inputBoxFaze2 !== null) {
    inputBoxRychlost.addEventListener("input", function () {
        rychlostval = Number(this.value);

        if (id !== null) {
            clearInterval(id);
            id = setInterval(animace, rychlostval);
        }

        drawImage(faze1val, faze2val, uhelvalX, uhelvalY);
    });
}

function animace() {

    if (rotateX == true) {
        uhelvalX = uhelvalX + 0.01;
        if (uhelvalX % 10 == 0) { uhelvalX = uhelvalX + 0.01 }
    }

    if (rotateY == true) {
        uhelvalY = uhelvalY + 0.01;
        if (uhelvalY % 10 == 0) { uhelvalY = uhelvalY + 0.01 }
    }

    drawImage(faze1val, faze2val, uhelvalX, uhelvalY);
}

function onRotateXclick() {
    let checkbox = document.querySelector("#rotateX");

    rotateX = checkbox.checked;
}

function onRotateYclick() {
    let checkbox = document.querySelector("#rotateY");
    rotateY = checkbox.checked;
}

function onbtnanimaceclick() {
    let btnanimace = document.querySelector("#btnanimace");

    if (id == null) {
        id = setInterval(animace, rychlostval);
        btnanimace.textContent = 'Zastav animaci';
    }
    else {
        clearInterval(id);
        btnanimace.textContent = 'Spust animaci';
        id = null
    }
}

function onbtnExample1click() {
    drawImage(46, 69, 0, 0);
}

function onbtnExample2click() {
    drawImage(92, 69, 0, 0);
}

function onbtnExample3click() {
    drawImage(52, 65, 0, 0);
}

function onbtnExample4click() {
    drawImage(206, 46, 0, 0);
}

function onbtnExample5click() {
    let f1 = 'aaa';
    drawImage(f1, 49, 0, 0);
}

function wrapText(context, text, x, y, line_width, line_height) {
    let line = '';
    let paragraphs = text.split('\n');
    for (var i = 0; i < paragraphs.length; i++) {
        let words = paragraphs[i].split(' ');
        for (var n = 0; n < words.length; n++) {
            let testLine = line + words[n] + ' ';
            let metrics = contex.measureText(testLine);
            let testWidth = metrics.width;
            if (testWidth > line_width && n > 0) {
                contex.fillText(line, x, y);
                line = words[n] + ' ';
                y += line_height;
            }
            else {
                line = testLine;
            }
        }
        contex.fillText(line, x, y);
        y += line_height;
        line = '';
    }
}

function drawErrorMessage(errormessage) {
    contex.beginPath();
    contex.clearRect(0, 0, contex.canvas.width, contex.canvas.height);
    contex.fillStyle = "red";
    contex.font = "14px Georgia";

    wrapText(contex, errormessage, 20, 30, contex.canvas.width - 20, 20);

    contex.stroke();
    contex.closePath();
}

function drawImage(paramfaze1, paramfaze2, paramuhelX, paramuhelY) {
    let i = 0;

    let widthc = 0;
    let heightc = 0;

    try {
        widthc = document.querySelector('.grid').children[0].clientWidth;
    } catch (error) {
        drawErrorMessage('Class ".grid" nebyla nalezena');
        return;
    }

    try {
        heightc = document.querySelector('#form').children[0].clientHeight;
    } catch (error) {
        drawErrorMessage("Identifikator \"#form\" nebyl nalezen ");
        return;
    }

    if (isNaN(paramfaze1)) {
        drawErrorMessage('Hodnota parametru "Faze 1" funkce drawImage() "' + paramfaze1 + '" neni ciselna hodnota.\n\nObrazec nebude vykreslen');
        return;
    }

    if (isNaN(paramfaze2)) {
        drawErrorMessage('Hodnota parametru "Faze 2" funkce drawImage() "' + paramfaze2 + '" neni ciselna hodnota.\n\nObrazec nebude vykreslen');
        return;
    }

    contex.canvas.width = widthc;
    contex.canvas.height = heightc;

    if (paramfaze1 !== faze1val) {
        faze1val = paramfaze1;

        let inputBox = document.querySelector("#faze1");
        if (inputBox == null) {
            drawErrorMessage("Identifikator \"#faze1\" nebyl nalezen ");
            return;
        }
        else {
            inputBox.value = faze1val;
        }
    }


    if (paramfaze2 !== faze2val) {
        faze2val = paramfaze2;

        let inputBox = document.querySelector("#faze2");
        if (inputBox == null) {
            drawErrorMessage("Identifikator \"#faze2\" nebyl nalezen ");
            return;
        }
        else {
            inputBox.value = faze2val;
        }
    }

    if (paramuhelX !== uhelvalX) {
        uhelvalX = paramuhelX;
    }

    if (paramuhelY !== uhelvalY) {
        uhelvalY = paramuhelY;
    }

    contex.lineWidth = 0.2;
    contex.strokeStyle = 'green';

    contex.beginPath();
    contex.clearRect(0, 0, widthc, heightc);

    posunX = Math.trunc((widthc - 20) / 2);
    posunY = Math.trunc((heightc - 20) / 2);

    while (i < 720) {
        i = i + 0.5;

        x = Math.trunc(Math.sin(i * paramfaze1 + paramuhelY) * posunX + posunX + 10);
        y = Math.trunc(Math.cos(i * paramfaze2 + paramuhelX) * posunY + posunY + 10);

        if (i >= 0.5) {
            contex.lineTo(x, y);
        }
        else {
            contex.moveTo(x, y)
        }
    }

    contex.stroke();
    contex.closePath();
}

window.onload = function () {
    drawImage(faze1val, faze2val, uhelvalX, uhelvalY);
};

window.onresize = function () {
    drawImage(faze1val, faze2val, uhelvalX, uhelvalY);
};