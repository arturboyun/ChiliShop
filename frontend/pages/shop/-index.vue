<template>
  <div class='shop'>
    <categories-bar :categories='headerCategories'/>
    <products :category_title='""' :products='[]'/>
  </div>
</template>

<script>
import ProductsGrid from '@/components/sections/shop/Products'
import CategoriesBar from '@/components/sections/shop/CategoriesBar'
import { mapActions, mapGetters } from 'vuex'
import Products from '@/components/sections/shop/Products'

export default {
  name: 'Shop',
  components: { Products, CategoriesBar, ProductsGrid },
  async asyncData() {
    return {
    }
  },
  computed: {
    ...mapGetters('categories', ['headerCategories'])
  },
  methods: {
    ...mapActions('categories', ['getCategoryBySlug'])
  }
}
</script>

<style lang='scss' scoped>
.shop {
  min-height: 70vh;
  padding: 50px 270px;
  display: flex;
  background-color: #080808;
}
</style>
