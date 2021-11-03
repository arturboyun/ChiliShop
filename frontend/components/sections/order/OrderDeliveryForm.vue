<template>
  <div class='delivery_form'>
    <h2 class='delivery_form__title'>Данные для отправки</h2>

    <ValidationObserver v-slot='{ invalid }'>
      <form class='form' @submit.prevent='onSubmit'>
        <div class='form_col'>
          <label class='label'>
            <span class='label__text'>Ваш Город*</span>
            <ValidationProvider v-slot='{ errors }' rules='required'>
              <input v-model='city' :class='{error: errors[0]}' class='input' type='text'>
              <span class='input__errors'>{{ errors[0] }}</span>
            </ValidationProvider>
          </label>

          <label class='label'>
            <span class='label__text'>Способ доставки*</span>
            <ValidationProvider v-slot='{ errors }' rules='required'>
              <b-select v-model='delivery' :class='{error: errors[0]}'>
                <option value=''>Выберите способ</option>
                <option
                  v-for='option in delivery_options'
                  :key='option.value'
                  :value='option.value'
                >
                  {{ option.text }}
                </option>
              </b-select>
              <span class='input__errors'>{{ errors[0] }}</span>
            </ValidationProvider>
          </label>

          <label class='label' v-if='delivery === "branch"'>
            <span class='label__text'>Отделение*</span>
            <ValidationProvider v-slot='{ errors }' rules='required'>
              <input v-model='branch_number' :class='{error: errors[0]}' class='input' type='text'>
              <span class='input__errors'>{{ errors[0] }}</span>
            </ValidationProvider>
          </label>

          <div class='courier_data' v-if='delivery === "courier"'>
            <label class='label'>
              <span class='label__text'>Улица*</span>
              <ValidationProvider v-slot='{ errors }' rules='required'>
                <input v-model='street' :class='{error: errors[0]}' class='input' type='text'>
                <span class='input__errors'>{{ errors[0] }}</span>
              </ValidationProvider>
            </label>

            <div class='courier_data__row'>
              <label class='label' v-if='delivery === "courier"'>
                <span class='label__text'>Дом*</span>
                <ValidationProvider v-slot='{ errors }' rules='required'>
                  <input v-model='house' :class='{error: errors[0]}' class='input' type='text'>
                  <span class='input__errors'>{{ errors[0] }}</span>
                </ValidationProvider>
              </label>
              <label class='label' v-if='delivery === "courier"'>
                <span class='label__text'>Кв.*</span>
                <ValidationProvider v-slot='{ errors }' rules='required'>
                  <input v-model='apartment' :class='{error: errors[0]}' class='input' type='text'>
                  <span class='input__errors'>{{ errors[0] }}</span>
                </ValidationProvider>
              </label>
            </div>
          </div>
        </div>

        <div class='form_col'>
          <label class='label'>
            <span class='label__text'>Способ оплаты*</span>
            <ValidationProvider v-slot='{ errors }' rules='required|alpha'>
              <b-select v-model='payment_method' :class='{error: errors[0]}'>
                <option value=''>Выберите способ</option>
                <option
                  v-for='option in payment_method_options'
                  :key='option.value'
                  :value='option.value'
                >
                  {{ option.text }}
                </option>
              </b-select>
              <span class='input__errors'>{{ errors[0] }}</span>
            </ValidationProvider>
          </label>

          <label class='label'>
            <span class='label__text'>Комментарий к заказу</span>
            <textarea v-model='comment' class='input'>asddsadsa</textarea>
<!--            <span class='input__errors'>{{ errors[0] }}</span>-->
          </label>

          <button class='btn' type="submit" :disabled="invalid">ОФОРМИТЬ ЗАКАЗ</button>
        </div>
      </form>
    </ValidationObserver>
  </div>
</template>

<script>
import { ValidationObserver, ValidationProvider } from 'vee-validate'
import { getDeliveryData, getPersonalData, saveDeliveryData } from '~/utils'

export default {
  name: 'OrderDeliveryForm',
  components: { ValidationProvider, ValidationObserver },
  data() {
    return {
      city: '',
      delivery: '',
      payment_method: '',
      comment: '',
      branch_number: '',
      street: '',
      house: '',
      apartment: '',
      delivery_options: [
        { value: 'branch', text: 'Доставка в отделение( Новая Почта)' },
        { value: 'courier', text: 'Доставка курьером( Новая Почта)' }
      ],
      payment_method_options: [
        { value: 'imposed', text: 'Наложенный платеж' },
        { value: 'card', text: 'Оплатить картой Visa/Mastercard' }
      ]
    }
  },
  mounted() {
    const data = getDeliveryData()
    if (data) {
      this.city = data.city
      this.delivery = data.delivery
      this.payment_method = data.payment_method
      this.comment = data.comment
      this.branch_number = data.branch_number
      this.street = data.street
      this.house = data.house
      this.apartment = data.apartment
    }
  },
  methods: {
    onSubmit() {
      const deliveryData = {
        city: this.city,
        delivery: this.delivery,
        payment_method: this.payment_method,
        comment: this.comment,
        branch_number: this.branch_number,
        street: this.street,
        house: this.house,
        apartment: this.apartment,
      }
      saveDeliveryData(deliveryData)
      this.$emit('form-completed', deliveryData)
    }
  }
}
</script>

<style lang='scss' scoped>

.delivery_form {
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

    .courier_data {
      display: flex;
      flex-direction: column;

      .courier_data__row {
        display: flex;

        label:first-child {
          margin-right: 34px;
        }
      }
    }
    @media screen and (max-width: 1200px) {
      flex-direction: column;

      .btn {
        margin-bottom: 25px;
      }
    }
  }
}
</style>
