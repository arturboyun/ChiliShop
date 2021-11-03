<template>
  <div class='header'>
    <burger-button class='burger'/>
    <NuxtLink to='/'><img alt='chili logo' class='logo' src='@/assets/images/logo.png'></NuxtLink>

    <div class='menu'>
      <nav class='menu__nav'>
        <ul class='nav-list'>
          <li v-if="categories.length > 0" class='nav-list__item'>
            <NuxtLink
              v-for='category in categories'
              :key='category.id'
              :to='`/shop/category/${category.slug}`'
            >
              {{ category.name }}
            </NuxtLink>
          </li>
          <li v-else>Категорий нет.</li>
        </ul>
      </nav>
      <button class='basket_btn' @click='openBasket'>
        <BasketIcon />
      </button>
    </div>
  </div>
</template>

<script>
import BasketIcon from '~/assets/icons/basket.svg?inline'
import BurgerButton from "./BurgerButton";

export default {
  name: 'Header',
  components: { BasketIcon, BurgerButton },
  data() {
    return {
      basketItemsCount: 0
    }
  },
  props: {
    categories: {
      type: Array,
      required: true
    }
  },
  computed: {},
  methods: {
    openBasket() {
      this.$emit('open-basket')
    }
  },
  watch: {}
}
</script>

<style lang='scss' scoped>
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

  @media screen and (max-width: 1200px) {
    padding: 0 16px;
    height: 70px;

    .logo {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
  }

  @media screen and (max-width: 1750px) {
    padding: 0 120px;
  }

  @media screen and (max-width: 1375px) {
    padding: 0 45px;
  }
}

.menu {
  display: flex;
  &__nav {
    display: flex;
    align-items: center;

    .nav-list {
      display: flex;
      margin-right: 70px;

      :not(:last-child) {
        margin-right: 40px;
      }
    }

    @media screen and (max-width: 1200px) {
      display: none;
    }
  }
}

.basket_btn {
  position: relative;

  .basket_items_count {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    bottom: -2px;
    right: -5px;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background-color: #fff;
    font-size: 10px;
    line-height: 5px;
    font-weight: 600;
  }
}
</style>
