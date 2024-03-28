var fotodef = 0;
var fotolijst1 = ["assets/images/Mooie_links_UDR.jpg", "assets/images/UDR_B.jpg"]// foto bestanden
 
function veranderafbeelding1() {// deze functie zorgt ervoor dat de foto veranderd
    var defleppard = document.getElementById("afbeelding1");// je moet wel nog even alle variabele namen veranderen
    defleppard.src = fotolijst1[fotodef];
    fotodef = (fotodef + 1) % fotolijst1.length;
}