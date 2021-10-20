<template>
  <div class='personal_form'>
    <h2 class='personal_form__title'>Данные для отправки</h2>

    <ValidationObserver v-slot='{ invalid }'>
      <form class='form' @submit.prevent="onSubmit">
        <div class='form_col'>
          <label class='label'>
            <span class='label__text'>Ваше имя*</span>
            <ValidationProvider v-slot='{ errors }' rules='required|alpha'>
              <input v-model='first_name' :class='{error: errors[0]}' class='input' type='text'>
              <span class='input__errors'>{{ errors[0] }}</span>
            </ValidationProvider>
          </label>

          <label class='label'>
            <span class='label__text'>Ваша фамилия*</span>
            <ValidationProvider v-slot='{ errors }' rules='required|alpha'>
              <input v-model='last_name' :class='{error: errors[0]}' class='input' type='text'>
              <span class='input__errors'>{{ errors[0] }}</span>
            </ValidationProvider>
          </label>
        </div>

        <div class='form_col'>
          <label class='label'>
            <span class='label__text'>Телефон*</span>
            <ValidationProvider v-slot='{ errors }' rules='required'>
              <input v-model='phone' :class='{error: errors[0]}' class='input' placeholder='380997774422' type='text'>
              <span class='input__errors'>{{ errors[0] }}</span>
            </ValidationProvider>
          </label>

          <label class='label'>
            <span class='label__text'>E-mail*</span>
            <ValidationProvider v-slot='{ errors }' rules='required|email'>
              <input v-model='email' :class='{error: errors[0]}' class='input' type='text'>
              <span class='input__errors'>{{ errors[0] }}</span>
            </ValidationProvider>
          </label>

          <button class='btn' type="submit" :disabled="invalid">Продолжить</button>
        </div>
      </form>
    </ValidationObserver>
  </div>
</template>

<script>
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import { getPersonalData, savePersonalData } from '~/utils'

export default {
  name: 'OrderPersonalForm',
  components: { ValidationProvider, ValidationObserver },
  data() {
    return {
      first_name: '',
      last_name: '',
      phone: '',
      email: ''
    }
  },
  mounted() {
    const data = getPersonalData()
    this.first_name = data.first_name
    this.last_name = data.last_name
    this.phone = data.phone
    this.email = data.email
  },
  methods: {
    onSubmit() {
      savePersonalData({
        first_name: this.first_name,
        last_name: this.last_name,
        phone: this.phone,
        email: this.email,
      })
      this.$emit('form-completed')
    }
  }
}
</script>

<style lang='scss' scoped>
.personal_form {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-right: 77px;

  &__title {
    font-size: 20px;
    line-height: 24px;
    border-bottom: 2px solid #fff;
    padding-bottom: 11px;
    margin-bottom: 32px;
  }

  .form {
    display: flex;
    width: 100%;

    .form_col {
      display: flex;
      flex-direction: column;
      width: 100%;

      &:first-child {
        margin-right: 109px;
      }
    }

    .label {
      display: flex;
      flex-direction: column;
      width: 100%;
      margin-bottom: 0;

      input::placeholder {
        color: #575757;
      }

      &__text {
        font-weight: 200;
        font-size: 18px;
        line-height: 22px;
        color: #fff;
        margin-bottom: 10px;
      }
    }

    .btn {
      width: 100%;
      height: 50px;
      font-weight: 500;
      font-size: 14px;
      line-height: 17px;
      letter-spacing: 0.13em;
      background-color: #fff;
      color: #000;

      &:disabled {
        background-color: #a8a8a8;
        cursor: default;
      }
    }
  }
}
</style>
