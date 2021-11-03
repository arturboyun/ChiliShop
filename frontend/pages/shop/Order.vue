<template>
  <div class='order'>
    <h1 v-if='!personal_form_completed || !delivery_form_completed' class='order__title'>Оформление заказа</h1>
    <div class='order__blocks'>
      <order-personal-form
        v-if='!personal_form_completed'
        @form-completed='personalFormComplete'
      />
      <order-delivery-form
        v-if='personal_form_completed && !delivery_form_completed'
        @form-completed='deliveryFormComplete'
      />
      <order-info v-if='!personal_form_completed || !delivery_form_completed' />
      <order-completed v-if='personal_form_completed && delivery_form_completed' />
    </div>
  </div>
</template>

<script>
import OrderPersonalForm from '@/components/sections/order/OrderPersonalForm'
import OrderInfo from '@/components/sections/order/OrderInfo'
import OrderDeliveryForm from '~/components/sections/order/OrderDeliveryForm'
import OrderCompleted from '~/components/sections/order/OrderCompleted'
import { api } from '@/api'
import { mapState } from 'vuex'


export default {
  name: 'Order',
  components: { OrderCompleted, OrderDeliveryForm, OrderInfo, OrderPersonalForm },
  data() {
    return {
      personal_form_completed: false,
      delivery_form_completed: false
    }
  },
  computed: {
    ...mapState('basket', ['items']),
    itemsSumPrice() {
      let sum = 0
      this.items.forEach((item) => {
        sum += item.product.price * item.quantity
      })
      return sum
    }
  },
  methods: {
    personalFormComplete() {
      this.personal_form_completed = true
    },
    async deliveryFormComplete(data) {
      if (data.payment_method === 'card') {
        const productNames = []
        const productPrices = []
        const productCounts = []
        this.items.forEach(item => {
          productNames.push(item.product.title)
          productPrices.push(item.product.price)
          productCounts.push(item.quantity)
        })
        console.log(productNames)
        console.log(await api.createInvoice(this.itemsSumPrice, productNames, productPrices, productCounts))
      }
      this.delivery_form_completed = true
    }
  }
}
</script>

<style lang='scss' scoped>
.order {
  background-color: #080808;
  min-height: 80vh;
  padding: 45px 270px;

  .order__title {
    text-align: center;
    font-size: 24px;
    margin-bottom: 46px;
    text-transform: uppercase;
  }

  .order__blocks {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    width: 100%;
  }

  @media screen and (max-width: 1750px) {
    padding: 98px 120px 45px 45px;
  }

  @media screen and (max-width: 1375px) {
    padding: 98px 45px 45px 45px;
  }

  @media screen and (max-width: 1200px) {
    padding: 40px 15px;

    .order__title {
      font-size: 18px;
    }

    .order__blocks {
      flex-direction: column;
    }
  }
}
</style>
