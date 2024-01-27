var slideIndex = 1
showSlides(slideIndex)

// Next/previous controls
function plusSlides (n) {
  showSlides((slideIndex += n))
}

// Thumbnail image controls
function currentSlide (n) {
  showSlides((slideIndex = n))
}

function showSlides (n) {
  var i
  var slides = document.getElementsByClassName('home-detail-image')
  if (n > slides.length) {
    slideIndex = 1
  }
  if (n < 1) {
    slideIndex = slides.length
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none'
  }
  slides[slideIndex - 1].style.display = 'block'
}

// Reservation Handleer
const form = document.getElementById('reservation-form')
const full_name = document.getElementById('full_name_reservation')
const phone_no = document.getElementById('phone_no_reservation')
const date = document.getElementById('date_reservation')

form.addEventListener('submit', e => {
  e.preventDefault()

  if (validateReservationInputs() == true) {
    form.submit()
  }
})

const validateReservationInputs = () => {
  full_name_value = full_name.value.trim()
  phone_no_value = phone_no.value.trim()
  date_value = date.value.trim()

  if (full_name_value === '' || full_name_value === null) {
    setError(full_name, "Full name can't be empty!")
    return false
  } else if (phone_no_value === '' || phone_no_value === null) {
    setError(phone_no, "Phone number can't be empty!")
    return false
  } else if (date_value === '' || date_value === null) {
    setError(date, "Date can't be empty!")
    return false
  } else {
    return true
  }
}

const setError = (element, message) => {
  const parent = element.parentElement
  var displayError = parent.querySelector('#error-message')
  displayError.innerText = message
  parent.classList.add('error')
  parent.classList.remove('success')
}
