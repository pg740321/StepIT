function ButtonStartClick(ButtonID) {
var mess = "";

    if (ButtonID == 1) {
        mess = "starter \n $10 per \n month"
} else {
        mess = "econom \n $30 per \n month"        
}

window.confirm([mess]);
}