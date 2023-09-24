let canvas = document.getElementById("myCanvas")
let image = document.querySelector(".imageCanvas")
let form = document.querySelector(".form")
let selcolor = document.querySelector(".selcolor")
canvas.height = window.innerHeight
canvas.width = window.innerWidth
let ctx = canvas.getContext("2d")
ctx.lineWidth = 5

let prvky = Array();
let prvekTyp = 1;
let prvekWidth = 0;
let prvekHeight = 0;

let prevX = null
let prevY = null

let draw = false
let prvekColor = '#12732F';


let rectBtn = document.querySelector(".btnRect")
rectBtn.addEventListener("click", () => {
    nastavPrvek(1);
})

let arcBtn = document.querySelector(".btnCircle")
arcBtn.addEventListener("click", () => {
    nastavPrvek(2);
})

let lineBtn = document.querySelector(".btnLine")
lineBtn.addEventListener("click", () => {
    nastavPrvek(3);
})

let ellipseBtn = document.querySelector(".btnEllipse")
ellipseBtn.addEventListener("click", () => {
    nastavPrvek(4);
})

function clearScr() {
    ctx.beginPath();
    ctx.strokeStyle = prvekColor;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.stroke()
}

let newBtn = document.querySelector(".btnNew")
newBtn.addEventListener("click", () => {
    prvky = [];
    clearScr();
})

function nastavPrvek(cislo) {
    prvekTyp = cislo;

    if (prvekTyp == 1) {
        rectBtn.style.color = 'orange';
        rectBtn.style.borderStyle = 'inset';
    }
    else {
        rectBtn.style.color = '';
        rectBtn.style.borderStyle = 'outset';
    }

    if (prvekTyp == 2) {
        arcBtn.style.color = 'orange';
        arcBtn.style.borderStyle = 'inset';
    }
    else {
        arcBtn.style.color = '';
        arcBtn.style.borderStyle = 'outset';
    }

    if (prvekTyp == 3) {
        lineBtn.style.color = 'orange';
        lineBtn.style.borderStyle = 'inset';
    }
    else {
        lineBtn.style.color = '';
        lineBtn.style.borderStyle = 'outset';
    }


    if (prvekTyp == 4) {
        ellipseBtn.style.color = 'orange';
        ellipseBtn.style.borderStyle = 'inset';
    }
    else {
        ellipseBtn.style.color = '';
        ellipseBtn.style.borderStyle = 'outset';
    }

}

selcolor.addEventListener("input", (event) => {
    prvekColor = event.target.value;
});

let saveBtn = document.querySelector(".btnSave")
saveBtn.addEventListener('click', async () => {
    let text = prvky.toString();

    const opts = {
        types: [{
            suggestedName: 'Hodnoty.pct',
            description: 'Picture file',
            accept: { 'Picture/PCT': ['.pct'] },
        }],
    };

    const fileHandle = await window.showSaveFilePicker(opts);
    console.log(fileHandle.kind, fileHandle.name);

    const writable = await fileHandle.createWritable();
    await writable.write(text);
    await writable.close();
});

let loadBtn = document.querySelector(".btnLoad")
loadBtn.addEventListener('click', async () => {
    let text = prvky.toString();

    const opts = {
        types: [{
            suggestedName: 'Hodnoty.pct',
            description: 'Picture file',
            accept: { 'Picture/PCT': ['.pct'] },
        }],
    };

    const [fileHandle] = await window.showOpenFilePicker(opts);   
    const fileData = await fileHandle.getFile();

    text = await fileData.text(); 
    prvky=text.split(',');

    clearScr();
    vykresliprvky();
});

function vykresliprvek(value) {
    const myArray = value.split(';');

    let pTyp = parseInt(myArray[0]);
    let pColor = myArray[1];

    let paramX = parseInt(myArray[2]);
    let paramY = parseInt(myArray[3]);
    let paramW = parseInt(myArray[4]);
    let paramH = parseInt(0);

    if (myArray.length > 5)
        paramH = parseInt(myArray[5]);

    ctx.beginPath();
    ctx.strokeStyle = pColor;

    switch (pTyp) {
        case 1: {
            ctx.moveTo(paramX, paramY);
            ctx.rect(paramX, paramY, paramW, paramH);
            break;
        }

        case 2: {
            ctx.arc(paramX, paramY, paramW, 0, 2 * Math.PI, true);
            break;
        }

        case 3: {
            ctx.moveTo(paramX, paramY);
            ctx.lineTo(paramX + paramW, paramY + paramH);
            break;
        }

        case 4: {
            ctx.ellipse(paramX, paramY, paramW, paramH, Math.PI / 4, 0, 2 * Math.PI, true);
            break;
        }
    }
    ctx.stroke()
}

function vykresliprvky() {
    prvky.forEach(vykresliprvek);
}

image.addEventListener("mousedown", (e) => {
    draw = true;
})

image.addEventListener("mouseup", (e) => {

    if (draw) {
        switch (prvekTyp) {
            case 1: {
                prvky.push(prvekTyp + ";" + prvekColor + ";" + prevX + ";" + prevY + ";" + prvekWidth + ";" + prvekHeight);
                break;
            }

            case 2: {
                prvky.push(prvekTyp + ";" + prvekColor + ";" + prevX + ";" + prevY + ";" + prvekWidth);
                break;
            }

            case 3: {
                prvky.push(prvekTyp + ";" + prvekColor + ";" + prevX + ";" + prevY + ";" + prvekWidth + ";" + prvekHeight);
                break;
            }

            case 4: {
                prvky.push(prvekTyp + ";" + prvekColor + ";" + prevX + ";" + prevY + ";" + prvekWidth + ";" + prvekHeight);
                break;
            }
        }
    }

    draw = false;
})

function mousePositionOnCanvas(e) {
    var el = e.target, c = el;
    var scaleX = c.width / c.offsetWidth || 1;
    var scaleY = c.height / c.offsetHeight || 1;

    if (!isNaN(e.offsetX))
        return { x: e.offsetX * scaleX, y: e.offsetY * scaleY };

    var x = e.pageX, y = e.pageY;
    do {
        x -= el.offsetLeft;
        y -= el.offsetTop;
        el = el.offsetParent;
    } while (el);
    return { x: x * scaleX, y: y * scaleY };
}

image.addEventListener("mousemove", function (e) {

    var x = mousePositionOnCanvas(e).x;
    var y = mousePositionOnCanvas(e).y;

    if (prevX == null || prevY == null || !draw) {
        prevX = x;
        prevY = y;
        return
    }

    if (draw) {
        prvekWidth = x - prevX;
        prvekHeight = y - prevY;

        clearScr();
        vykresliprvky();

        try {
            switch (prvekTyp) {
                case 1: {
                    vykresliprvek(prvekTyp + ";" + prvekColor + ";" + prevX + ";" + prevY + ";" + prvekWidth + ";" + prvekHeight);
                    break;
                }

                case 2: {
                    vykresliprvek(prvekTyp + ";" + prvekColor + ";" + prevX + ";" + prevY + ";" + prvekWidth);
                    break;
                }

                case 3: {
                    vykresliprvek(prvekTyp + ";" + prvekColor + ";" + prevX + ";" + prevY + ";" + prvekWidth + ";" + prvekHeight);
                    break;
                }
                case 4: {
                    if (prvekWidth < 0) { prvekWidth = -1 * prvekWidth };
                    if (prvekHeight < 0) { prvekHeight = -1 * prvekHeight };

                    ctx.moveTo(prevX, prevY);
                    vykresliprvek(prvekTyp + ";" + prvekColor + ";" + prevX + ";" + prevY + ";" + prvekWidth + ";" + prvekHeight);
                    break;
                }
            }

        } catch (error) {

        }
    }
})

window.onload = function () {
    selcolor.value = '#12732F';
    nastavPrvek(1);
}