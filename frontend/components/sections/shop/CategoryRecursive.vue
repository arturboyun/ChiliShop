<template>
  <li>
    <nuxt-link :key='category.id' :to='`/shop/category/${category.slug}`' class='name'>{{ category.name }}</nuxt-link>
    <ul class='sub_categories'>
      <category-recursive
        v-for='category in category.children'
        :key='category.id'
        :category='category'
      />
    </ul>
  </li>
</template>

<script>
export default {
  name: 'CategoryRecursive',
  props: {
    category: { type: Object, required: true }
  }
}
</script>

<style lang='scss' scoped>
.name {
  white-space: nowrap;
}

.nuxt-link-exact-active,
.nuxt-link-active {
  font-weight: 500;
}

.sub_categories > li {
  margin-left: 12px;
  white-space: nowrap;
}
</style>
