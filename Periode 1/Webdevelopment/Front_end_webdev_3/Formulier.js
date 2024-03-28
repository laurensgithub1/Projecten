function validateForm() {
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var lname = document.getElementById('Tnummer').value;
    var email = document.getElementById('Email').value;
    var bericht = document.getElementById('Bericht').value;

    if (fname === '' || lname === '' || Tnummer === '' || email === '' || bericht === '') {
        alert('Vul alle verplichte velden in: voornaam, achternaam, telefoonummer, e-mail en bericht.');
        return false;
    }
    if (bericht.length > 200) {
        alert('Het bericht mag niet meer dan 200 tekens bevatten.');
        return false;
    }
    return true;
}