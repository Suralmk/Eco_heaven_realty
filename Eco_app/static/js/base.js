// this.window.onload(() => {
//   var anonomous_id = 12
//   localStorage.setItem('anonomous_id', anonomous_id)
// })

//fixed nav bar
const headerNav = document.querySelector('.nav-container')
const heroContainer = document.querySelector('.hero-container')
if (window.scrollY > 0) {
  headerNav.classList.add('sticky')
  heroContainer.classList.add('hero-contain')
} else {
  headerNav.classList.remove('sticky')
}

// Mobile Menu
const navHandler = () => {
  navBar.classList.toggle('stick', this.window.scrollY > 100)
}
const navBar = document.querySelector('.mobile-nav-container')
window.addEventListener('scroll', navHandler)

function displayMobileMenu () {
  const menu = document.getElementById('mobile-menu')
  menu.classList.toggle('active')
}

//scroll to top page
const topBtn = document.querySelector('.scroll-to-top-btn')
if (window.pageYOffset > 100) {
  topBtn.classList.add('active-top-btn')
} else {
  topBtn.classList.remove('active-top-btn')
}

//expandable content of  frequently asked questions
const title = document.querySelectorAll('.answer-to-questions')
title.forEach(title => {
  title.addEventListener('click', () => {
    title.classList.toggle('active')
  })
})
