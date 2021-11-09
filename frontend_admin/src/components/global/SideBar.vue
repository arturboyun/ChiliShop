<template>
  <div class="sidebar" :class="{ open: isOpen }">
    <it-icon box class="icon menu" name="menu" @click="toggle" />

    <router-link
      v-for="(item, index) in menuItems"
      :key="index"
      class="link"
      :to="item.to"
    >
      <it-tooltip placement="right" :disabled="isOpen">
        <template #content>{{ item.name }}</template>
        <it-icon box :class="['icon', item.iconClass]" :name="item.icon" />
      </it-tooltip>

      <p class="text">{{ item.name }}</p>
    </router-link>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'SideBar',
  setup() {
    let menuItems = ref([
      { name: 'Панель', icon: 'dashboard', iconClass: 'dashboard', to: '/' },
      {
        name: 'Заказы',
        icon: 'shopping_basket',
        iconClass: 'orders',
        to: '/orders',
      },
      {
        name: 'Товары',
        icon: 'local_offer',
        iconClass: 'products',
        to: '/products',
      },
      {
        name: 'Категории',
        icon: 'sort',
        iconClass: 'categories',
        to: '/categories',
      },
    ]);
    let isOpen = ref(false);
    const toggle = () => (isOpen.value = !isOpen.value);
    return { isOpen, menuItems, toggle };
  },
};
</script>

<style scoped lang="scss">
.sidebar {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 15px;
  height: 100vh;
  background-color: #2a2a2a;
  //margin-right: 15px;
  border-radius: 0 12px 12px 0;
  transition: 0.5s ease;
  overflow: hidden;
  width: 65px;
  box-shadow: 3px 0 6px rgba(#000, 0.45);

  &.open {
    width: 10%;
  }

  .text {
    //white-space: nowrap;
  }

  .link {
    width: 100%;
    display: flex;
    align-items: center;

    &:hover .icon {
      transform: scale(1.15);
    }
  }

  .link:not(:last-child) {
    margin-bottom: 15px;
  }

  .icon {
    background-color: #26292d;
    color: #fff;
    margin-right: 15px;
    transition: 0.35s ease;

    &.menu {
      font-size: 25px;
      padding: 4px;
      margin: 0 0 15px;
      cursor: pointer;
    }

    &.dashboard {
      background-color: #6065be;
    }

    &.orders {
      background-color: #6fbe60;
    }

    &.products {
      background-color: #c94e4e;
    }

    &.categories {
      background-color: #c9984e;
    }
  }
}
</style>
