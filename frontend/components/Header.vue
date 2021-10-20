<template>
  <div class="header">
    <NuxtLink to="/"><img src="@/assets/images/logo.png" alt="chili logo" class="logo"></NuxtLink>

    <nav>
      <ul class="nav-list">
        <li class="nav-list__item">
          <client-only>
            <NuxtLink
              v-for='category in categories'
              :to="`/shop/category/${category.slug}`"
              :key='category.id'
            >
              {{ category.name }}
            </NuxtLink>
          </client-only>
        </li>
      </ul>
      <button class="basket_btn" @click='openBasket'>
        <BasketIcon/>
      </button>
    </nav>
  </div>
</template>

<script>
import BasketIcon from '~/assets/icons/basket.svg?inline'

export default {
  name: "Header",
  components: {BasketIcon},
  data() {
    return {
      basketItemsCount: 0
    }
  },
  props: {
    categories: {
      type: Array,
      required: true,
    },
  },
  computed: {
  },
  methods: {
    openBasket() {
      this.$emit('open-basket')
    }
  },
  watch: {
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
