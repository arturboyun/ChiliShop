import { extend } from 'vee-validate'
import { alpha, email, required, digits, regex } from 'vee-validate/dist/rules'

extend('email', {
  ...email,
  message: 'Это поле должно содержать E-Mail.'
})

extend('regex', regex)

extend('required', {
  ...required,
  message: 'Это поле обязательно.'
})

extend('alpha', {
  ...alpha,
  message: 'Это поле должно содержать только буквы.'
})

extend('digits', {
  ...digits,
  message: 'Это поле должно содержать только цыфры.'
})
