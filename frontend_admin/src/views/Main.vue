<template>
  <SideBar v-if="$store.getters.isLoggedIn" />
  <div class="page">
    <router-view />
  </div>
  <UserInfo v-if="username" :name="username" />
  <div class="theme-button">
    <it-toggle v-model="toggleValue" :options="toggleOptions" icons round />
  </div>
</template>

<script>
import store from '@/store';
import SideBar from '@/components/global/SideBar';
import UserInfo from '@/components/global/UserInfo';
import { ref, computed } from 'vue';
import { useStore } from 'vuex';

const routeGuardMain = async (to, from, next) => {
  await store.dispatch('testToken');
  await store.dispatch('getMe');
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
  components: { SideBar, UserInfo },
  beforeRouteEnter(to, from, next) {
    routeGuardMain(to, from, next);
  },
  beforeRouteUpdate(to, from, next) {
    routeGuardMain(to, from, next);
  },
  setup() {
    const store = useStore();
    const username = computed(() => store.getters.getUsername);
    const toggleOptions = ref(['wb_sunny', 'bedtime']);
    return { toggleOptions, toggleValue: ref('wb_sunny'), username };
  },
};
</script>

<style lang="scss">
.page {
  width: 100%;
  overflow: hidden;
  padding: 28px 28px 28px 89px;
  transition: all 0.3s ease;
}

.theme-button {
  display: none;
  position: fixed;
  bottom: 15px;
  right: 25px;
}
</style>
