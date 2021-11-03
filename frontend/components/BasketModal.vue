<template>
  <div v-if='show' class='modal' @click.stop='hideModal'>
    <div class='modal__content' @click.stop>
      <div class='close_btn' @click.stop='hideModal'>
        <CloseIcon />
      </div>
      <div v-if='items.length > 0' class='basket'>
        <h2 class='title'>Корзина</h2>
        <div class='items'>
          <div
            v-for='(item, index) in items'
            :key='index'
            class='basket__item'
          >
            <div :style='`background-image: url("${parseFirstImageURL(item.product.images)}");`' class='product_image'></div>
            <div class='product_info'>
              <div>
                <div class='title'>{{ item.product.title }}</div>
                <div class='size'>Размер: <span>{{ item.size }}</span></div>
              </div>
              <div>
                <div class='quantity'>
                  <button class='quantity__button' @click='decreaseCount(item)'>-</button>
                  <span>{{ item.quantity }}</span>
                  <button class='quantity__button' @click='increaseCount(item)'>+</button>
                </div>
                <button class='delete_item_button' @click='deleteProduct(item)'>Удалить</button>
              </div>
            </div>
            <div class='price'>
              {{ item.product.price * item.quantity }} ₴
            </div>
          </div>
        </div>
        <div class='sum'>
          <h3 class='sum__title'>Общая стоимость:</h3>
          <div class='sum__price'>
            {{ itemsSumPrice }} ₴
          </div>
        </div>
        <div class='buttons'>
          <button class='btn continue_button' @click.stop='hideModal'>Продолжить покупки</button>
          <NuxtLink class='btn checkout_button' to='/shop/order'>Оформить заказ</NuxtLink>
        </div>
      </div>
      <div v-else class='basket'>
        <div class='title'>Корзина</div>
        <div class='no_products'>Ваша корзина пуста.</div>
      </div>
    </div>
  </div>
</template>

<script>
import toggleMixin from '@/mixins/toggleMixin'
import CloseIcon from '@/assets/icons/close.svg?inline'
import * as utils from '@/utils'

export default {
  name: 'BasketModal',
  mixins: [toggleMixin],
  components: { CloseIcon },
  data() {
    return {
      items: []
    }
  },
  created() {
    this.items = utils.getBasketItems()
    console.log('created')
  },
  mounted() {
    this.items = utils.getBasketItems()
    console.log('mounted')
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
    }
  }
}
</script>

<style lang='scss' scoped>
.modal {
  position: fixed;
  width: 100%;
  height: 100vh;
  top: 0;
  left: 0;
  background-color: rgba(#000000, .5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1002;

  .modal__content {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;

    @media screen and (max-width: 720px) {
      min-width: 100%;
      min-height: 100vh;
      //padding: 16px 21px;
      //justify-content: flex-start;
    }

    .close_btn {
      position: absolute;
      right: 13px;
      top: 15px;
      cursor: pointer;
    }
  }
}


.basket {
  width: 100%;
  background-color: #222222;
  padding: 30px 45px 35px;
  display: flex;
  flex-direction: column;
  align-items: center;

  @media screen and (max-width: 720px) {
    width: 100%;
    height: 100vh;
    padding: 16px 21px;
    justify-content: flex-start;
  }

  .title {
    font-weight: 600;
    font-size: 24px;
    line-height: 29px;
    color: #fff;
    text-transform: uppercase;
    text-align: center;
  }

  .items {
    display: flex;
    flex-direction: column;
    width: 100%;
    max-height: 625px;
    overflow-y: auto;
    margin-bottom: 15px;
    padding-right: 5px;

    &::-webkit-scrollbar {
      width: 6px;

    }

    &::-webkit-scrollbar-thumb {
      background-color: #fff;
    }
  }

  .no_products {
    width: 400px;
    height: 200px;
    text-align: center;
  }
}

.basket__item {
  position: relative;
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 27px;

  @media screen and (max-width: 720px) {
    justify-content: flex-start;
  }

  .product_image {
    width: 117px;
    height: 160px;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    @media screen and (max-width: 720px) {
      min-width: 87px;
      min-height: 119px;
      margin-right: 18px;
      justify-content: flex-start;
    }
  }

  .product_info {
    display: flex;
    width: 230px;
    flex-direction: column;
    justify-content: space-between;

    @media screen and (max-width: 720px) {
      margin-right: 9px;
    }

    .title {
      font-weight: 500;
      font-size: 20px;
      line-height: 24px;
      margin-bottom: 10px;
      text-align: left;

      @media screen and (max-width: 720px) {
        font-size: 14px;
      }
    }

    .size {
      font-weight: 300;
      font-size: 16px;
      line-height: 20px;
      margin-bottom: 45px;

      @media screen and (max-width: 720px) {
        font-size: 14px;
        margin-bottom: 11px;
      }

      span {
        font-weight: 500;
        text-transform: uppercase;
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
    }
  }

  .price {
    width: 100px;
    display: flex;
    justify-content: flex-end;
    align-items: flex-end;
    align-self: center;
    justify-self: flex-end;
    font-weight: 300;
    font-size: 24px;
    line-height: 29px;
    color: #fff;
    white-space: nowrap;

    @media screen and (max-width: 720px) {
      position: absolute;
      top: 70px;
      right: 15px;
      font-weight: 300;
      font-size: 15px;
      line-height: 17px;
    }
  }
}

.sum {
  display: flex;
  justify-content: space-between;
  width: 100%;
  border-bottom: 2px solid #fff;
  padding-bottom: 8px;
  margin-bottom: 41px;

  .sum__title {
    font-weight: 300;
    font-size: 24px;
    line-height: 29px;
  }

  .sum__price {
    font-weight: 500;
    font-size: 24px;
    line-height: 29px;
  }
}

.buttons {
  display: flex;
  justify-content: space-between;
  width: 100%;

  .continue_button {
    box-shadow: none;
    background-color: rgba(#fff, 0);
    font-weight: 500;
    font-size: 14px;
    line-height: 17px;
    letter-spacing: 0.13em;
    margin-right: 25px;
    cursor: pointer;

    &:hover {
      color: #000;
      background-color: rgba(#fff, .7);
    }
  }

  .checkout_button {
    color: #000;
    background-color: #fff;
    font-weight: 500;
    font-size: 14px;
    line-height: 17px;
    letter-spacing: 0.13em;
    cursor: pointer;

    &:hover {
      color: #fff;
      background-color: rgba(#fff, 0);
    }
  }

  @media screen and (max-width: 720px) {
    flex-direction: column;

    .continue_button,
    .checkout_button {
      width: 100%;
      margin: 0;
    }

    .continue_button {
      margin-bottom: 18px;
    }
  }
}
</style>
