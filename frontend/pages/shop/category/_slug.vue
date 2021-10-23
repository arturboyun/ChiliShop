<template>
  <div class='shop'>
    <categories-bar :categories='this.headerCategories' />
    <products
      v-if='this.category.products.length > 0'
      :category_title='this.category.title'
      :products='this.products'
    />
    <div class='not-found' v-else>Товаров не найдено.</div>
  </div>
</template>

<script>
import CategoriesBar from '@/components/sections/shop/CategoriesBar'
import Products from '@/components/sections/shop/Products'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'CategoryPage',
  components: { Products, CategoriesBar },
  async asyncData({ params, store }) {
    const slug = params.slug
    const category = await store.dispatch('categories/getCategoryBySlug', { slug })
    const products = await store.dispatch('products/getProductsByCategorySlug', { slug })
    return { slug, category, products }
  },
  mounted() {
    this.$nuxt.$emit('close-menu')
  },
  computed: {
    ...mapGetters('categories', ['headerCategories'])
  },
  methods: {
    ...mapActions('categories', ['getCategoryBySlug'])
  }
}
</script>

<style scoped lang='scss'>
.shop {
  width: 100%;
  min-height: 70vh;
  padding: 50px 270px;
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  background-color: #080808;

  @media screen and (max-width: 1200px) {
    padding: 50px 15px;
  }
}
</style>
