const changeEmail = document.getElementById('change-email-form')

try {
  changeEmail.addEventListener('submit', e => {
    e.preventDefault()
    if (changeEmailValidation()) {
      changeEmail.submit()
    }
  })
} catch (err) {}

function changeEmailValidation () {
  var input,
    i,
    valid = true
  input = changeEmail.getElementsByTagName('input')
  for (i = 0; i < input.length; i++) {
    if (input[i].value == '') {
      input[i].classList.add('invalid')
      input[i].parentElement.querySelector('#errormessage').innerHTML =
        'Email is required!'
      input[i].style.border = '1px solid  rgba(180, 11, 11, 0.753)'
      input[i].classList.remove('valid')
      valid = false
    } else {
      input[i].classList.add('valid')
      input[i].classList.remove('invalid')
    }
  }
  return valid // return the valid status
}

// Change Passswod form Validation

const changePassword = document.getElementById('change-password-form')

try {
  changePassword.addEventListener('submit', e => {
    e.preventDefault()
    if (changePasswordForm()) {
      changePassword.submit()
    }
  })
} catch (err) {}

function changePasswordForm () {
  var input,
    i,
    valid = true
  input = changePassword.getElementsByTagName('input')
  for (i = 0; i < input.length; i++) {
    if (input[i].value == '') {
      input[i].classList.add('invalid')
      input[i].parentElement.querySelector('#errormessage').innerHTML =
        'Password is required!'
      input[i].style.border = '1px solid  rgba(180, 11, 11, 0.753)'
      input[i].classList.remove('valid')
      valid = false
    } else {
      input[i].classList.add('valid')
      input[i].classList.remove('invalid')
    }
  }
  return valid // return the valid status
}

//Edit name form Validation
// Change Passswod form Validation

const editName = document.getElementById('edit-name-form')

try {
  editName.addEventListener('submit', e => {
    e.preventDefault()
    if (editNameValidation()) {
      editName.submit()
    }
  })
} catch (err) {}

function editNameValidation () {
  var input,
    i,
    valid = true
  input = editName.getElementsByTagName('input')
  for (i = 0; i < input.length; i++) {
    if (input[i].value == '') {
      input[i].classList.add('invalid')
      input[i].parentElement.querySelector('#errormessage').innerHTML =
        'This field is required!'
      input[i].style.border = '1px solid  rgba(180, 11, 11, 0.753)'
      input[i].classList.remove('valid')
      valid = false
    } else {
      input[i].classList.add('valid')
      input[i].classList.remove('invalid')
    }
  }
  return valid // return the valid status
}
