var fotodef = 0;
var fotolijst2 = ["assets/images/UDR_links.jpg", "assets/images/Traxxas_udr_blauw.jpg"]// foto bestanden
 
function veranderafbeelding2() {// deze functie zorgt ervoor dat de foto veranderd
    var defleppard = document.getElementById("afbeelding2");// je moet wel nog even alle variabele namen veranderen
    defleppard.src = fotolijst2[fotodef];
    fotodef = (fotodef + 1) % fotolijst2.length;
}