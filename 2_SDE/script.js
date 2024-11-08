const correctUsername = "root";
const correctPassword = "root";

function validateLogin() {
    const enteredUsername = document.getElementById("username").value;
    const enteredPassword = document.getElementById("password").value;

    if (enteredUsername === correctUsername && enteredPassword === correctPassword) {
        alert("API: 12345678-abcd-1234-efgh-567890abcdef");
        return true;
    } else {
        alert("Incorrect username or password.");
        return false;
    }
}
