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

let inputBox = document.querySelector("#faze1");
inputBox.addEventListener("input", function () {
    faze1val = this.value;
    drawImage(faze1val, faze2val, uhelvalX, uhelvalY);
});

let inputBox2 = document.querySelector("#faze2");
inputBox2.addEventListener("input", function () {
    faze2val = this.value;
    drawImage(faze1val, faze2val, uhelvalX, uhelvalY);
});

let rychlostBox = document.querySelector("#rychlost");
rychlost.addEventListener("input", function () {
    rychlostval = Number(this.value);

    if (id !== null) {
        clearInterval(id);
        id = setInterval(animace, rychlostval);
    }

    drawImage(faze1val, faze2val, uhelvalX, uhelvalY);
});


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
    drawImage(46, 69, uhelvalX, uhelvalY);
}

function onbtnExample2click() {
    drawImage(98, 49, uhelvalX, uhelvalY);
}

function onbtnExample3click() {
    drawImage(52, 65, uhelvalX, uhelvalY);
}

function onbtnExample4click() {
    drawImage(206, 46, uhelvalX, uhelvalY);
}

function drawImage(paramfaze1, paramfaze2, paramuhelX, paramuhelY) {
    let i = 0;

    let form = document.querySelector("#form");

    if (form.clientWidth > 728) {
        contex.canvas.width = Math.trunc(form.clientWidth * 0.8);
    }
    else {
        contex.canvas.width = Math.trunc(form.clientWidth * 0.98);
    }
    contex.canvas.height = form.clientHeight;

    if (paramfaze1 !== faze1val) {
        faze1val = paramfaze1;

        let inputBox = document.querySelector("#faze1");
        inputBox.value = faze1val;
    };

    if (paramfaze2 !== faze2val) {
        faze2val = paramfaze2;

        let inputBox = document.querySelector("#faze2");
        inputBox.value = faze2val;
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
    contex.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight);

    posunX = Math.trunc((canvas.clientWidth - 20) / 2);
    posunY = Math.trunc((canvas.clientHeight - 20) / 2);

    while (i < 720) {
        i = i + .5;

        x = Math.trunc(Math.sin(i * paramfaze1 + paramuhelY) * posunX + posunX + 10);
        y = Math.trunc(Math.cos(i * paramfaze2 + paramuhelX) * posunY + posunY + 10);

        if (i <= .2) contex.moveTo(x, y)
        else
            contex.lineTo(x, y);
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