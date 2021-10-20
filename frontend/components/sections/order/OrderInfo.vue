<template>
  <div class='order_info'>
    <h2 class='order_info__title'>Ваш заказ</h2>
    <div v-if='items.length > 0' class='items'>
      <div
        v-for='item in items'
        :key='item.product.id'
        class='items__item'
      >
        <div :style='`background-image: url("${item.product.images[0].src}");`' class='item__image' />

        <div class='item__info'>
          <div>
            <div class='title'>{{ item.product.title }}</div>
            <div class='size'>Размер: <span>{{ item.size }}</span></div>
          </div>
            <div class='quantity'>
              <button class='quantity__button' @click='decreaseCount(item)'>-</button>
              <span>{{ item.quantity }}</span>
              <button class='quantity__button' @click='increaseCount(item)'>+</button>
            </div>
          <div>
            <button class='delete_item_button' @click='deleteProduct(item)'>Удалить</button>
          </div>
        </div>

        <div class='item__price'>
          {{ item.product.price * item.quantity }} ₴
        </div>
      </div>
    </div>
    <div v-else class='items_not_found'>У вас в корзине нет товаров.</div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'OrderInfo',
  beforeMount() {
    this.refreshStateItems();
    this.$nuxt.$emit('close-basket');
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
    ...mapActions('basket', ['refreshStateItems', 'addItem', 'removeItem', 'decreaseProductQuantity']),
    increaseCount(item) {
      this.addItem({ product: item.product, size: item.size, quantity: 1 })
    },
    deleteProduct(item) {
      this.removeItem({ product_id: item.product.id })
    },
    decreaseCount(item) {
      this.decreaseProductQuantity(item.product.id)
    },
    closeModal() {
      this.$root.$emit('close')
    }
  }
}
</script>

<style lang='scss' scoped>
.order_info {
  &__title {
    font-size: 20px;
    line-height: 24px;
    border-bottom: 2px solid #fff;
    padding-bottom: 11px;
    margin-bottom: 32px;
  }
}

.items {
  max-height: 330px;
  padding-right: 14px;
  overflow-y: scroll;

  &::-webkit-scrollbar {
    width: 6px;

  }

  &::-webkit-scrollbar-track {

  }

  &::-webkit-scrollbar-thumb {
    background-color: #fff;
  }

  &__item {
    width: 450px;
    display: flex;
    margin-bottom: 29px;

    .item__image {
      width: 106px;
      height: 145px;
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;
      margin-right: 18px;
    }

    .item__info {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      margin-right: 50px;

      .title {
        font-weight: 500;
        font-size: 14px;
        line-height: 17px;
        color: #fff;
        margin-bottom: 10px;
      }

      .size {
        font-weight: 300;
        font-size: 14px;
        line-height: 17px;
        margin-bottom: 17px;

        span {
          font-weight: 500;
          font-size: 14px;
          line-height: 17px;
          text-transform: uppercase;
        }
      }
    }

    .quantity {
      display: flex;
      margin-bottom: 5px;

      span {
        margin-right: 14px;
      }

      .quantity__button {
        display: flex;
        align-items: center;
        justify-content: center;
        color: #fff;
        width: 23px;
        height: 23px;
        border: 1px solid #fff;

        &:not(:last-child) {
          margin-right: 14px;
        }
      }
    }

    .delete_item_button {
      font-family: Montserrat, sans-serif;
      color: #fff;
      font-weight: 300;
      font-size: 16px;
      line-height: 20px;
      text-decoration: underline;
    }

    .item__price {
      font-weight: 300;
      font-size: 18px;
      line-height: 22px;
      white-space: nowrap;
    }
  }
}
</style>
