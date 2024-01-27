// Show Side menu Nav
const sideMenu = document.getElementById('mySidenav')
const openNav = () => {
  sideMenu.classList.add('side-menu-active')
}
const closeNav = () => {
  sideMenu.classList.remove('side-menu-active')
}

// show Sub menu items
const menu = document.querySelectorAll('.menu-item-btn')
menu.forEach(element => {
  element.addEventListener('click', () => {
    var menuItem = element.parentElement
    menuItem.querySelector('ul').classList.toggle('active')
  })
})

// Home add , image Upload Btn
const chooseImage = document.querySelector('.staff-home-add-image-select')
const ImageChoose = document.getElementById('home_image')
// chooseImage.addEventListener('click', () => {
//   ImageChoose.click()
// })

// Show Uploaded Image
const showUploadedImage = event => {
  if (event.target.files.length > 0) {
    var imageUrl = URL.createObjectURL(event.target.files[0])
    var UploadedImagePreview = document.getElementById('uploaded-image-preview')
    UploadedImagePreview.src = imageUrl
    UploadedImagePreview.style.display = 'block'
    console.log(event.target.files)
  } else {
    console.log('no')
  }
}

// Show Manay Uploaded Image
const showImagesContainer = document.querySelector('.show-uploaded-images')
const showUploadedImages = event => {
  var i
  var files = event.target.files

  if (files.length > 0) {
    for (i = 0; i < files.length; i++) {
      let imageContainer = document.createElement('div')
      showImagesContainer.appendChild(imageContainer)
      let image = document.createElement('img')
      imageContainer.appendChild(image)
      imageUrl = URL.createObjectURL(files[i])
      image.src = imageUrl
    }
  } else {
    return
  }
}

function filterUsers () {
  // Declare variables
  var input, filter, table, tr, name, i, txtValue, email, emailValue
  input = document.getElementById('filter_users')
  filter = input.value.toUpperCase()
  table = document.getElementById('users_table')
  tr = table.getElementsByTagName('tr')

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    name = tr[i].getElementsByTagName('td')[1]
    email = tr[i].getElementsByTagName('td')[2]

    if (name || email) {
      txtValue = name.textContent || name.innerText
      emailValue = email.textContent || email.innerText

      if (
        txtValue.toUpperCase().indexOf(filter) > -1 ||
        emailValue.toUpperCase().indexOf(filter) > -1
      ) {
        tr[i].style.display = ''
      } else {
        tr[i].style.display = 'none'
      }
    }
  }
}
//Staff Message Show

const messagebox = document.querySelector('.staff-messages')

const messageShow = event => {
  event.preventDefault()
  messagebox.classList.add('messages-show')
  setTimeout(() => {
    messagebox.classList.remove('messages-show')
  }, 4000)
}

/*--------------------------------------
    Validation of forms in staff page
----------------------------------------*/

// Validation for Add New Home Member
const addHomeForm = document.getElementById('add-new-home')
try {
  addHomeForm.addEventListener('submit', e => {
    e.preventDefault()

    if (addHomeValidation()) {
      addHomeForm.submit()
    }
  })
} catch (err) {}

function addHomeValidation () {
  var input,
    i,
    valid = true
  input = addHomeForm.getElementsByClassName('input')
  for (i = 0; i < input.length; i++) {
    if (input[i].value == '') {
      input[i].classList.add('invalid')
      input[i].classList.remove('valid')
      valid = false
    } else {
      input[i].classList.add('valid')
      input[i].classList.remove('invalid')
    }
  }
  return valid
}

// Validation for Add Staff Member
const addStaffForm = document.getElementById('add-staff-form')
try {
  addStaffForm.addEventListener('submit', e => {
    e.preventDefault()
    if (addStaffUserValidation()) {
      addStaffForm.submit()
    }
  })
} catch (err) {}

function addStaffUserValidation () {
  var input,
    i,
    valid = true
  input = addStaffForm.getElementsByClassName('input')
  for (i = 0; i < input.length; i++) {
    if (input[i].value == '') {
      input[i].classList.add('invalid')
      input[i].classList.remove('valid')
      valid = false
    } else {
      input[i].classList.add('valid')
      input[i].classList.remove('invalid')
    }
  }
  return valid // return the valid status
}

// Validation for  Blog Create form
const blogAddForm = document.getElementById('blog-add-form')
try {
  blogAddForm.addEventListener('submit', e => {
    e.preventDefault()
    if (addBlogValidation()) {
      blogAddForm.submit()
    }
  })
} catch (err) {}

function addBlogValidation () {
  var input,
    i,
    valid = true
  input = blogAddForm.getElementsByClassName('input')

  for (i = 0; i < input.length; i++) {
    if (input[i].value == '') {
      input[i].classList.add('invalid')
      input[i].classList.remove('valid')
      valid = false
    } else {
      input[i].classList.add('valid')
      input[i].classList.remove('invalid')
    }
  }
  return valid // return the valid status
}
