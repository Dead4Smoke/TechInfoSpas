const reg_button = document.querySelector('.reg-button')
const text = document.querySelector('#promo-text')
const form = document.querySelector('.test')

function Jopa () {
  text.style.display = "none"
  form.style.display = "block"
  reg_button.setAttribute('onclick', 'Popa()')

}

function Popa () {
  text.style.display = "block"
  form.style.display = "none"
  reg_button.setAttribute('onclick', 'Jopa()')
}
