/* 
Write the code which asks for a login with prompt.
If the visitor enters "Admin", then prompt for a password, 
if the input is an empty line or Esc – show “Canceled”, if 
it’s another string – then show “I don’t know you”.
The password is checked as follows:
    If it equals “TheMaster”, then show “Welcome!”,
    Another string – show “Wrong password”,
    For an empty string or cancelled input, show “Canceled”
*/

let user = prompt('Enter your username: ')

if (user === 'Admin') {
    var user_password = prompt('Enter your password')
    if (user_password === 'TheMaster') {
        alert('Welcome')
    } else if (user_password === '' || user_password == undefined) {
        alert('Cancelled')
    } else {
        alert('Wrong password')
    }
} else if (user === '' || user == undefined) {
    alert('Cancelled')
} else {
    alert("I don't know you")
}
