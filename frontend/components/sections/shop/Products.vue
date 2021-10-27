<template>
  <div class='products'>
    <h1 class='title'>{{ category_title }}</h1>
    <div class='products_grid'>
      <product-card
        v-for='product in products'
        :key='product.id'
        v-if='product.images.length > 0'
        :price='product.price'
        :image_url='product.images[0].src'
        :title='product.title'
        :slug='product.slug'
      />
    </div>
  </div>
</template>

<script>
import ProductCard from '@/components/sections/shop/ProductCard'

export default {
  name: 'Products',
  components: { ProductCard },
  props: {
    category_title: {
      type: String,
      required: true
    },
    products: {
      type: Array,
      required: true
    }
  }
}
</script>

<style lang='scss' scoped>
.products {
  display: flex;
  flex-direction: column;
  padding: 21px 38px;
  background-color: #1c1c1c;
  width: 100%;

  @media screen and (max-width: 720px) {
    padding: 21px 16px;
  }

  .title {
    font-size: 18px;
    font-weight: 500;
    line-height: 18px;
    color: #ffffff;
    margin-bottom: 31px;
  }

  .products_grid {
    width: 100%;
    display: grid;
    grid-gap: 48px 28px;
    grid-template-columns: 207px 207px 207px 207px;

    @media screen and (max-width: 1768px) {
      grid-template-columns: 207px 207px 207px;
    }

    @media screen and (max-width: 1620px) {
      grid-template-columns: 207px 207px;
    }

    @media screen and (max-width: 1200px) {
      grid-template-columns: 207px 207px 207px 207px;
    }

    @media screen and (max-width: 720px) {
      grid-template-columns: auto auto;
      grid-gap: 22px 22px;
    }
  }
}
</style>
