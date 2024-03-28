function validateForm() {
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var email = document.getElementById('Email').value;
    var bericht = document.getElementById('Bericht').value;

    if (fname === '' || lname === '' || email === '' || bericht === '') {
        alert('Vul alle verplichte velden in: voornaam, achternaam, e-mail en bericht.');
        return false;
    }

    return true;
}