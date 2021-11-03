<template>
  <div class='order_info'>
    <h2 class='order_info__title'>Ваш заказ</h2>
    <div v-if='items.length > 0' class='items'>
      <div
        v-for='(item, index) in items'
        :key='index'
        class='items__item'
      >
        <div class='item_col'>
          <div :style='`background-image: url("${parseFirstImageURL(item.product.images)}");`' class='item__image' />
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
        </div>

        <div class='item__price'>
          {{ item.product.price * item.quantity }} ₴
        </div>
      </div>
    </div>
    <div v-else class='items_not_found'>У вас в корзине нет товаров.</div>

    <div class='order_info__sum'>
      <div class='text'>Общая стоимость товаров:</div>
      <div class='sum'>{{ itemsSumPrice }} ₴</div>
    </div>
  </div>
</template>

<script>
import * as utils from '~/utils'

export default {
  name: 'OrderInfo',
  data() {
    return {
      items: [],
    }
  },
  created() {
    this.items = utils.getBasketItems()
    this.$nuxt.$emit('close-basket');
  },
  computed: {
    itemsSumPrice() {
      let sum = 0
      if (this.items) {
        this.items.forEach((item) => {
          sum += item.product.price * item.quantity
        })
      }
      return sum
    },
  },
  methods: {
    increaseCount(item) {
      utils.addItemToBasket(item.product, item.size, 1)
      this.items = utils.getBasketItems()
    },
    deleteProduct(item) {
      this.items = utils.removeBasketItem(item.product.id, item.size)
    },
    decreaseCount(item) {
      this.items = utils.decreaseProductQuantity(item.product.id, item.size)
    },
    parseFirstImageURL(images) {
      if (images.length > 0) {
        return images[0].src
      }
      return undefined
    },
    closeModal() {
      this.$root.$emit('close')
    }
  }
}
</script>

<style lang='scss' scoped>
.order_info {
  width: 80%;

  &__title,
  &__sum {
    font-size: 20px;
    line-height: 24px;
    white-space: nowrap;
  }
  &__title {
    border-bottom: 2px solid #fff;
    padding-bottom: 11px;
    margin-bottom: 32px;
  }

  &__sum {
    display: flex;
    justify-content: space-between;
    border-top: 2px solid #fff;
    padding-top: 11px;
    margin-top: 32px;
    width: 100%;

    .sum {
      font-weight: 500;
    }
  }

  @media screen and (max-width: 1200px) {
    width: 100%;
  }
}

.items {
  max-height: 330px;
  padding-right: 14px;
  overflow-y: scroll;

  &::-webkit-scrollbar {
    width: 6px;
  }

  &::-webkit-scrollbar-thumb {
    background-color: #fff;
  }

  &__item {
    width: 100%;
    display: flex;
    justify-content: space-between;
    margin-bottom: 29px;

    .item_col {
      display: flex;
    }

    .item__image {
      min-width: 106px;
      height: 145px;
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;
      margin-right: 18px;
    }

    .item__info {
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      margin-right: 18px;

      @media screen and (max-width: 1200px) {
        width: 120px;
      }

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
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        width: 60px;
        height: 23px;
        //margin-right: 14px;
        //border: 1px solid #fff;
      }

      .quantity__button {
        display: flex;
        align-items: center;
        justify-content: center;
        color: #fff;
        width: 23px;
        height: 23px;
        border: 1px solid #fff;
        //
        //&:not(:last-child) {
        //  margin-right: 14px;
        //}
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
      width: 80px;
      display: flex;
      justify-content: flex-end;
      align-items: flex-end;
      align-self: center;
      justify-self: flex-end;
      font-weight: 300;
      font-size: 18px;
      line-height: 22px;
      white-space: nowrap;
    }
  }
}
</style>
