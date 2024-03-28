var fotodef = 0;
var fotolijst3 = ["assets/images/UDR_boven.jpg", "assets/images/UDR_onder.jpg"]// foto bestanden
 
function veranderafbeelding3() {// deze functie zorgt ervoor dat de foto veranderd
    var defleppard = document.getElementById("afbeelding3");// je moet wel nog even alle variabele namen veranderen
    defleppard.src = fotolijst3[fotodef];
    fotodef = (fotodef + 1) % fotolijst3.length;
}