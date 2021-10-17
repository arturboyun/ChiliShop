<template>
  <div class="header">
    <NuxtLink to="/"><img src="@/assets/images/logo.png" alt="chili logo" class="logo"></NuxtLink>

    <nav>
      <ul class="nav-list">
        <li class="nav-list__item">
          <NuxtLink to='/shop'>Магазин</NuxtLink>
          <NuxtLink
            v-for='category in categories'
            :to="`/shop/category/${category.slug}`"
            :key='category.id'
          >
            {{ category.name }}
          </NuxtLink>
        </li>
<!--        <li class="nav-list__item"><NuxtLink to="/">Пижамы</NuxtLink></li>-->
<!--        <li class="nav-list__item"><NuxtLink to="/">Халаты</NuxtLink></li>-->
<!--        <li class="nav-list__item"><NuxtLink to="/">Купальники</NuxtLink></li>-->
<!--        <li class="nav-list__item"><NuxtLink to="/">SALE</NuxtLink></li>-->
      </ul>
      <button class="basket_btn">
        <BasketIcon/>
      </button>
    </nav>
  </div>
</template>

<script>
import BasketIcon from "~/assets/icons/basket.svg?inline";
export default {
  name: "Header",
  components: {BasketIcon},
  props: {
    categories: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style scoped lang="scss">
.header {
  position: fixed;
  width: 100%;
  height: 100px;
  padding: 0 270px;
  background-color: #1c1c1c;
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 1000;
}

nav {
  display: flex;
  align-items: center;

  .nav-list {
    display: flex;
    margin-right: 70px;

    :not(:last-child) {
      margin-right: 40px;
    }
  }
}
</style>
