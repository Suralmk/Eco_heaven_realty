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
const topBtn = document.querySelector('.scroll-to-top-btn')
const mobileNavBar = document.querySelector('.mobile-nav-container')
const navBar = document.querySelector('.nav-container')

const navHandler = () => {
  if (navBar) {
    navBar.classList.toggle('stick', this.window.scrollY > 100)
  }
  if (mobileNavBar) {
    mobileNavBar.classList.toggle('stick', this.window.scrollY > 100)
  }
}

const scrollToTopBtnHandler = () => {
  topBtn.classList.toggle('active-top-btn', this.window.scrollY > 100)
}

window.addEventListener('scroll', () => {
  navHandler()
  scrollToTopBtnHandler()
})

function displayMobileMenu () {
  const menu = document.getElementById('mobile-menu')
  menu.classList.toggle('active')
}

//expandable content of  frequently asked questions
const title = document.querySelectorAll('.answer-to-questions')
title.forEach(title => {
  title.addEventListener('click', () => {
    title.classList.toggle('active')
  })
})
