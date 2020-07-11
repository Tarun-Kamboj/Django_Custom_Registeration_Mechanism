// document.querySelector('#signup input#fname').onchange = function(){
//     if(document.querySelector('#signup input#fname').value === ""){
//         document.querySelector('#one .error').classList.add('show');
//         document.querySelector('#one .error p').innerText = "This field can't be empty"
//     }



const name = document.getElementById('fname')
const phone = document.getElementById('pnum')
const male = document.getElementById('rb1')
const female = document.getElementById('rb2')
const password = document.getElementById('pwd')
const confirmPassword = document.getElementById('pwdagain')
const form = document.getElementById('form')
const errorElement = document.getElementById('error')


form.addEventListener('submit', (e) => {
  let messages = []
  if (name.value === '' || name.value == null) {
    messages.push('Name is required')
  }
  if (phone.value.length !==10)
    messages.push('Phone number must be 10 digits long')

  if (!male.checked && !female.checked)
    messages.push('Gender not selected')

  if (password.value.length <= 6 || password.value.length >= 20) {
    messages.push('Password must be longer than 6 characters and less than 20 characters')
  }

  if (confirmPassword !== password) {
    messages.push('Passwords do not match')
  }

  if (messages.length > 0) {
    e.preventDefault()
    errorElement.innerText = messages.join(', ')
  }
})