<template>
  <div class='order'>
    <h1 class='order__title'  v-if='!personal_form_completed || !delivery_form_completed'>Оформление заказа</h1>
    <div class='order__blocks'>
      <order-personal-form
        v-if='!personal_form_completed'
        @form-completed='personalFormComplete'
      />
      <order-delivery-form
        v-if='personal_form_completed && !delivery_form_completed'
        @form-completed='deliveryFormComplete'
      />
      <order-info v-if='!personal_form_completed || !delivery_form_completed'/>
      <order-completed   v-if='personal_form_completed && delivery_form_completed'/>
    </div>
  </div>
</template>

<script>
import OrderPersonalForm from '@/components/sections/order/OrderPersonalForm'
import OrderInfo from '@/components/sections/order/OrderInfo'
import OrderDeliveryForm from '~/components/sections/order/OrderDeliveryForm'
import OrderCompleted from '~/components/sections/order/OrderCompleted'

export default {
  name: 'Order',
  components: { OrderCompleted, OrderDeliveryForm, OrderInfo, OrderPersonalForm },
  data() {
    return {
      personal_form_completed: false,
      delivery_form_completed: false,
    }
  },
  methods: {
    personalFormComplete() {
      this.personal_form_completed = true;
    },
    deliveryFormComplete(data) {
      if (data.payment_method === "card") {
        // TODO: redirect to LiqPay
      }
      this.delivery_form_completed = true;
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
  }

  .order__blocks {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    width: 100%;
  }
}
</style>
