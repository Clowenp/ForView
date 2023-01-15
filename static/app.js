// add click effect to animate hamburger menu//

const menu = document.querySelector('#mobile-menu')
const menuLinks = document.querySelector('.navbar__menu')

// Monitor for clicks //
 menu.addEventListener('click', function() {
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active');
 });