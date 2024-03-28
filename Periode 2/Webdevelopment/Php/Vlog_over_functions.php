<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Age Checker</title>
</head>
<body>

<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the user's age from the form
    $age = isset($_POST["age"]) ? intval($_POST["age"]) : 0;

    // Check if the age is above 18
    if ($age >= 18) {
        echo "<p>You are an adult.</p>";
    } else {
        echo "<p>You are not an adult.</p>";
    }
}
?>

<!-- HTML form to get the user's age -->
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
    <label for="age">Enter your age:</label>
    <input type="number" id="age" name="age" required>
    <button type="submit">Check</button>
</form>

</body>
</html>