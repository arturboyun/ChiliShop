<template>
  <div class="dashboard">Dashboard</div>
</template>

<script>
import { useStore } from 'vuex';
import store from '@/store';

const routeGuardDashboard = async (to, from, next) => {
  if (!store.getters.isLoggedIn) {
    next('/login');
  } else {
    next();
  }
};
export default {
  name: 'Home',
  beforeRouteEnter(to, from, next) {
    routeGuardDashboard(to, from, next);
  },
  setup() {
    const store = useStore();
    store.dispatch('getMe');
    return {};
  },
};
</script>
