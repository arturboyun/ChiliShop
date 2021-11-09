<template>
  <div class="sidebar" :class="{ open: isOpen }">
    <div class="menu-button">
      <it-icon box class="icon menu" name="menu" @click="toggle" />
    </div>
    <div class="links">
      <router-link
        v-for="(item, index) in menuItems"
        :key="index"
        class="link"
        :to="item.to"
      >
        <it-tooltip placement="right" :disabled="isOpen" hoverable>
          <template #content>{{ item.name }}</template>
          <it-icon box :class="['icon', item.iconClass]" :name="item.icon" />
        </it-tooltip>

        <p class="text">{{ item.name }}</p>
      </router-link>
    </div>

    <div class="logout-button">
      <it-tooltip placement="right" :disabled="isOpen">
        <template #content>Выход</template>
        <it-icon box class="icon logout" name="logout" @click="logout" />
      </it-tooltip>
      <p class="text">Выход</p>
    </div>
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
    const logout = () => console.log('logout pressed');
    return { isOpen, menuItems, toggle, logout };
  },
};
</script>

<style scoped lang="scss">
.sidebar {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  height: 100vh;
  background-color: #2a2a2a;
  border-radius: 0 12px 12px 0;
  transition: 0.5s ease;
  box-shadow: 3px 0 6px rgba(#000, 0.45);
  width: 64px;

  .menu-button {
    padding: 15px;

    .menu {
      font-size: 25px;
      padding: 4px;
      width: 100%;
      margin: 0;
      cursor: pointer;
    }
  }

  .logout-button {
    padding: 15px;
    margin-top: auto;
    width: 100%;
    overflow: hidden;
    color: #fff;
    display: flex;
    align-items: center;
    cursor: pointer;

    .logout {
      transform: rotate(180deg);
    }

    &:hover {
      color: #94c2ff;
      .logout {
        transform: rotate(180deg) scale(1.15);
      }
    }
  }

  .links {
    transition: 0.5s ease;
    overflow: hidden;
    width: 100%;
    padding: 15px;
  }

  &.open {
    width: 10%;
    .links,
    .logout-button {
      width: 100%;
    }
  }

  .link {
    width: 100%;
    display: flex;
    align-items: center;

    &:hover .icon {
      //border-radius: 15px;
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
