// Authentication Validation

const login = document.getElementById('login-form')

try {
  login.addEventListener('submit', e => {
    e.preventDefault()
    if (loginValidation()) {
      login.submit()
    }
  })
} catch (err) {}
function loginValidation () {
  var input,
    i,
    valid = true
  input = login.getElementsByTagName('input')
  for (i = 0; i < input.length; i++) {
    if (input[i].value == '') {
      input[i].classList.add('invalid')
      input[i].parentElement.querySelector('#errormessage').innerHTML =
        'This field is required!'
      input[i].classList.remove('valid')
      valid = false
    } else {
      input[i].classList.add('valid')
      input[i].classList.remove('invalid')
    }
  }
  return valid // return the valid status
}

// Sign Up form validation
const signup = document.getElementById('signup-form')
try {
  signup.addEventListener('submit', e => {
    e.preventDefault()
    console.log(signupValidation())
    if (signupValidation()) {
      signup.submit()
    }
  })
} catch (err) {}

function signupValidation () {
  var input,
    i,
    valid = true
  input = signup.getElementsByTagName('input')
  for (i = 0; i < input.length; i++) {
    if (input[i].value === '') {
      input[i].classList.add('invalid')
      input[i].parentElement.querySelector('#errormessage').innerHTML =
        'This field is required!'
      input[i].classList.remove('valid')
      valid = false
    }
    // } else if (input[i].name === 'email') {
    //   if (!trueEmail(input[i].value)) {
    //     input[i].classList.add('invalid')
    //     input[i].parentElement.querySelector('#errormessage').innerHTML =
    //       'enter a valid email!'
    //     input[i].classList.remove('valid')
    //   }
    //   valid = false
    // }
    // else if (input[i].name === 'password') {
    //   if (input[i].value.length < 8) {
    //     input[i].classList.add('invalid')
    //     input[i].parentElement.querySelector('#errormessage').innerHTML =
    //       'Password must not be less than 8 cahrachter'
    //     input[i].classList.remove('valid')
    //   }
    //   valid = false
    // }
    else {
      input[i].classList.add('valid')
      input[i].classList.remove('invalid')
    }
  }
  return valid // return the valid status
}

function trueEmail (email) {
  return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
    email
  )
}

// Reset Password validation
const resetPassword = document.getElementById('reset-password-form')

try {
  resetPassword.addEventListener('submit', e => {
    e.preventDefault()
    if (resetPasswordValidation()) {
      resetPassword.submit()
    }
  })
} catch (err) {}

function resetPasswordValidation () {
  var input,
    i,
    valid = true
  input = resetPassword.getElementsByTagName('input')
  for (i = 0; i < input.length; i++) {
    if (input[i].value == '') {
      input[i].classList.add('invalid')
      input[i].parentElement.querySelector('#errormessage').innerHTML =
        'Email is required!'
      input[i].classList.remove('valid')
      valid = false
    } else {
      input[i].classList.add('valid')
      input[i].classList.remove('invalid')
    }
  }
  return valid // return the valid status
}

// Create Password validation
const createPassword = document.getElementById('create-password-form')

try {
  createPassword.addEventListener('submit', e => {
    e.preventDefault()
    if (createPasswordFormValidation()) {
      createPassword.submit()
    }
  })
} catch (err) {}

function createPasswordFormValidation () {
  var input,
    i,
    newPass,
    valid = true

  input = createPassword.getElementsByTagName('input')
  for (i = 0; i < input.length; i++) {
    if (input[i].name === 'new-password') {
      newPass = input[i].value
    }
    if (input[i].value == '') {
      input[i].classList.add('invalid')
      input[i].parentElement.querySelector('#errormessage').innerHTML =
        'This field is required!'
      input[i].classList.remove('valid')
      valid = false
    } else if (input[i].name === 'confirm-password') {
      if (input[i].value !== newPass) {
        input[i].classList.add('invalid')
        input[i].parentElement.querySelector('#errormessage').innerHTML =
          "Password doesn't match!"
        input[i].classList.remove('valid')
        valid = false
      }
    } else {
      input[i].classList.add('valid')
      input[i].classList.remove('invalid')
    }
  }
  return valid // return the valid status
}
