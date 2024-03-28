function validateForm() {
    var Bask = document.getElementById('Bask').value;
    var Ball = document.getElementById('Ball').value;
    var Voet = document.getElementById('Voet').value;
    var Rcau = document.getElementById('Rcau').value;
    var Lego = document.getElementById('lego').value;
    var Knut = document.getElementById('Knut').value;
    var Spor = document.getElementById('Spor').value;
    var Paar = document.getElementById('Paar').value;
    var Scha = document.getElementById('Scha').value;
    var Dans = document.getElementById('Dans').value;

    if (Bask === '' || Ball === '' || Voet === '' || Rcau === '' || Lego === '' || Knut === '' || Spor === '' || Paar === '' || Scha === '' || Dans === '') {
        alert('Vul alle verplichte velden in: Basketball, Ballet, Voetbal, Rc auto, Lego, Knutselen, Sporten, Paardrijden, Schaken en Dansen.');
        return false;
    }

    if (Rcau.toUpperCase() === 'J' && Lego.toUpperCase() === 'J' && Spor.toUpperCase() === 'J') {
        alert('Gefeliciteerd! Je hebt mijn hobby\'s correct geraden!');
        return true;
    } else {
        alert('Helaas, je hebt niet alle hobby\'s correct geraden. Probeer opnieuw.');
        return false;
    }
}
