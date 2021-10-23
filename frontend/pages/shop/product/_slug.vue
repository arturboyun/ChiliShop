<template>
  <div v-if='this.product' class='product'>
    <div class='images'>
      <div class='other_images'>
        <div
          v-for='image in otherImages'
          :key='image.id'
          :style='`background-image: url("${image.src}")`'
          class='image'
        />
      </div>
      <div :style='`background-image: url("${this.product.images[0].src}")`' class='main_image'></div>
    </div>

    <div class='info'>
      <h1 class='title'>{{ this.product.title }}</h1>
      <div class='price'>{{ this.product.price }} ₴</div>
      <h2 class='sizes_title'>Размер</h2>
      <div class='sizes'>
        <div class='sizes_buttons'>
          <button
            v-for='size in this.product.sizes'
            :key='size'
            :class='{selected: selectedSize === size, error: sizeNotSelectedError}'
            class='size'
            @click='chooseSize(size)'
          >
            {{ size }}
          </button>
        </div>
        <nuxt-link to='/sizes' class='sizes_text'>Размерная сетка</nuxt-link>
      </div>

      <button class='btn large' @click='addToBasket'>
        Добавить в корзину
      </button>
    </div>
  </div>
  <div v-else class='product'>
    <div class='not-found'>Такого продукта не существует.</div>
  </div>
</template>

<script>
export default {
  name: 'ProductSlug',
  data() {
    return {
      selectedSize: '',
      sizeNotSelectedError: false
    }
  },
  async asyncData({ params, store }) {
    const slug = params.slug
    const product = await store.dispatch('products/getProductBySlug', { slug })
    return { slug, product }
  },
  computed: {
    otherImages() {
      return this.product.images.slice(1, 4)
    }
  },
  methods: {
    chooseSize(size) {
      this.selectedSize = size;
      this.sizeNotSelectedError = false;
    },
    addToBasket() {
      this.sizeNotSelectedError = !this.selectedSize
      if (!this.sizeNotSelectedError) {
        this.$store.dispatch('basket/addItem', {
          product: this.product,
          size: this.selectedSize,
          quantity: 1
        })
      }
      this.$nuxt.$emit('open-basket')
    }
  }
}
</script>

<style lang='scss' scoped>
.product {
  padding: 98px 270px;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;

  @media screen and (max-width: 1200px) {
    padding: 98px 15px;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  @media screen and (max-width: 1750px) {
    padding: 98px 120px;
  }

  @media screen and (max-width: 1375px) {
    padding: 98px 45px;
  }
}

.not-found {
  min-height: 45vh;
  color: #d94a4a;
}

.images {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  margin-right: 64px;

  @media screen and (max-width: 1200px) {
    margin-right: 0;
    margin-bottom: 54px;
    width: 100%;
  }

  .main_image {
    width: 393px;
    height: 536px;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    @media screen and (max-width: 600px) {
      width: 100%;
      height: 324px;
    }
  }

  .other_images {
    display: flex;
    flex-direction: column;
    margin-right: 36px;

    .image {
      width: 129px;
      height: 176px;
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;

      &:not(:last-child) {
        margin-bottom: 4px;
      }
    }

    @media screen and (max-width: 1200px) {
      margin-right: 16px;

      .image {
        width: 75px;
        height: 102px;

        &:not(:last-child) {
          margin-bottom: 9px;
        }
      }
    }
  }
}

.info {
  display: flex;
  flex-direction: column;

  @media screen and (max-width: 1200px) {
    .btn {
      margin: 0 auto;
    }
  }

  .title {
    color: #fff;
    font-weight: 500;
    font-size: 30px;
    margin-bottom: 34px;

    @media screen and (max-width: 1200px) {
      font-size: 20px;
      margin-bottom: 15px;
    }
  }

  .price {
    align-self: flex-end;
    font-size: 30px;
    font-weight: 500;

    @media screen and (max-width: 1200px) {
      font-size: 20px;
      margin-bottom: 0;
    }
  }

  .sizes_title {
    font-size: 24px;
    font-weight: 300;
    margin-bottom: 24px;
  }

  .sizes {
    display: flex;
    justify-content: space-between;
    margin-bottom: 86px;

    .sizes_text {
      font-size: 24px;
      line-height: 24px;
      font-weight: 500;
      white-space: nowrap;
      align-self: flex-end;
    }

    .sizes_buttons {
      display: flex;
      width: 100%;

      .size {
        display: flex;
        align-items: center;
        justify-content: center;
        min-width: 40px;
        min-height: 40px;
        padding: 0 12px;
        font-size: 24px;
        line-height: 24px;
        border: 1px solid #ffffff;
        color: #fff;
        text-transform: uppercase;

        &:hover,
        &.selected {
          background-color: #fff;
          color: #000;
        }

        &:not(:last-child) {
          margin-right: 20px;
        }

        &.error {
          border: 1px solid red;
          color: red;
        }
      }
    }
  }
}
</style>
