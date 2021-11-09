<template>
  <SideBar v-if="showSideBar" />
  <div class="page">
    <router-view />
  </div>
  <div class="theme-button">
    <it-toggle v-model="toggleValue" :options="toggleOptions" icons round />
  </div>
</template>

<script>
import store from '@/store';
import SideBar from '@/components/global/SideBar';
import { ref } from 'vue';

const routeGuardMain = async (to, from, next) => {
  if (!store.getters.isLoggedIn) {
    if (to.path !== '/login') {
      next('/login');
    } else {
      next();
    }
  } else {
    if (to.path === '/' || to.path === '/login') {
      next('/dashboard');
    } else {
      next();
    }
  }
};

export default {
  name: 'Main',
  components: { SideBar },

  beforeRouteEnter(to, from, next) {
    routeGuardMain(to, from, next);
  },
  beforeRouteUpdate(to, from, next) {
    routeGuardMain(to, from, next);
  },

  setup() {
    const showSideBar = ref(store.getters.isLoggedIn);
    const toggleOptions = ref(['wb_sunny', 'bedtime']);
    return { showSideBar, toggleOptions, toggleValue: ref('wb_sunny') };
  },
};
</script>

<style lang="scss">
.page {
  width: 100%;
  padding: 28px;
}

.theme-button {
  position: fixed;
  bottom: 18px;
  right: 18px;
}
</style>
