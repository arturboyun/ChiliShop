<template>
  <div class="sidebar" :class="{ open: isOpen }">
    <div class="menu-button">
      <it-icon
        box
        :class="['icon', 'menu', { open: isOpen }]"
        class=""
        name="menu"
        @click="toggle"
      />
      <it-icon
        box
        :class="['icon menu close', { open: isOpen }]"
        class=""
        name="close"
        @click="toggle"
      />
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
        <it-icon box class="icon logout" name="logout" @click="makeLogout" />
      </it-tooltip>
      <p class="text">Выход</p>
    </div>
  </div>
</template>

<script>
import { getCurrentInstance, ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

export default {
  name: 'SideBar',
  setup() {
    const app = getCurrentInstance();
    const store = useStore();
    const router = useRouter();

    const showMessage = app.appContext.config.globalProperties.$Message;

    let menuItems = ref([
      {
        name: 'Панель',
        icon: 'dashboard',
        iconClass: 'dashboard',
        to: '/dashboard',
      },
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

    const toggle = () => {
      isOpen.value = !isOpen.value;
      const page = document.querySelector('.page');
      if (isOpen.value) {
        page.style.padding = `28px 28px 28px ${280 + 25}px`;
      } else {
        page.style.padding = '28px 28px 28px 89px';
      }
    };
    const makeLogout = async () => {
      showMessage.warning({ text: 'Вы вышли.' });
      await store.dispatch('logout');
      await router.push('/');
    };
    return { isOpen, menuItems, toggle, makeLogout };
  },
};
</script>

<style scoped lang="scss">
.sidebar {
  position: fixed;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  height: 100vh;
  background-color: #2a2a2a;
  border-radius: 0 12px 12px 0;
  transition: 0.35s ease;
  box-shadow: 3px 0 6px rgba(#000, 0.45);
  width: 64px;

  .links {
    transition: 0.35s ease;
    overflow: hidden;
    width: 100%;
    padding: 15px;

    .link::before {
      content: '';
      position: absolute;
      height: 32px;
      background-color: #fff;
      width: 5px;
      left: 0;
      z-index: 2;
      border-radius: 0 5px 5px 0;
      transform: translateX(-5px);
      transition: 0.35s ease;
    }

    .link.router-link-active::before {
      transform: translateX(0px);
    }
  }

  &.open {
    width: 280px;
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

  .menu-button {
    position: relative;
    width: 64px;
    height: 64px;
    .menu {
      position: absolute;
      font-size: 25px;
      padding: 4px;
      margin: 0;
      cursor: pointer;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      transition: 0.2s ease;

      &.open {
        opacity: 0;
        visibility: hidden;
        transform: translate(calc(-50% - 30px), -50%);
      }
    }

    .menu.close {
      opacity: 0;
      visibility: hidden;
      transform: translate(calc(-50% + 30px), -50%);

      &.open {
        opacity: 1;
        visibility: visible;
        transform: translate(-50%, -50%);
      }
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
      // transform: rotate(0deg);
    }

    &:hover {
      color: #94c2ff;
      .logout {
        transform: rotate(-180deg) scale(1.15);
      }
    }
  }

  .menu-button,
  .logout-button {
    .icon:hover {
      color: #d5cdf3;
    }
  }
}
</style>
