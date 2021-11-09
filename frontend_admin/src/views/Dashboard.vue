<template>
  <div class="dashboard">Dashboard</div>
</template>

<script>
import { useStore } from 'vuex';

export default {
  name: 'Home',
  setup() {
    const store = useStore();
    store.dispatch('getMe');
    return {};
  },
};
</script>
