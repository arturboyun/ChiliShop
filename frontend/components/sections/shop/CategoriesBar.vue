<template>
  <div class='categories'>
    <h2 class='title'>Категории</h2>
    <ul>
      <li v-for='category in categories'>
        <nuxt-link :to='`/shop/category/${category.slug}`' :key='category.id' class='name'>{{ category.name }}</nuxt-link>
        <!--        <ul class='sub_categories'>-->
        <!--          <li>-->
        <!--            <div class='name'>Category</div>-->
        <!--            <ul class='sub_categories'></ul>-->
        <!--          </li>-->
        <!--        </ul>-->
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'CategoriesBar',
  props: {
    categories: { type: Array, required: true }
  }
}
</script>

<style lang='scss' scoped>

.categories {
  width: 20%;
  margin-bottom: 15px;

  .title {
    font-size: 18px;
    font-weight: 500;
    line-height: 18px;
    color: #ffffff;
    margin-bottom: 31px;
  }

  .sub_categories > li {
    margin-left: 25px;
  }
}

</style>
