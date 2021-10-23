<template>
  <div class='categories'>
    <h2 class='title'>Категории</h2>
    <ul>
      <category-recursive  v-for='category in categories' :key='category.id' :category='category'/>
    </ul>
  </div>
</template>

<script>
import CategoryRecursive from '@/components/sections/shop/CategoryRecursive'
export default {
  name: 'CategoriesBar',
  components: { CategoryRecursive },
  props: {
    categories: { type: Array, required: true }
  },
}
</script>

<style lang='scss' scoped>

.categories {
  margin-bottom: 15px;
  margin-right: 98px;

  @media screen and (max-width: 1200px) {
    display: none;
  }

  .title {
    font-size: 18px;
    font-weight: 500;
    line-height: 18px;
    color: #ffffff;
    margin-bottom: 31px;
    white-space: nowrap;
  }
}

</style>
