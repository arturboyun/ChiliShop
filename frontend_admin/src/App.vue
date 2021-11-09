<template>
  <SideBar />

  <div class="page">
    <router-view />
  </div>

  <div class="theme-button">
    <it-toggle v-model="toggleValue" :options="toggleOptions" icons round />
  </div>
</template>

<script>
import { ref } from 'vue';
import SideBar from '@/components/global/SideBar';

export default {
  components: { SideBar },
  setup() {
    const toggleOptions = ref(['wb_sunny', 'bedtime']);
    return { toggleOptions, toggleValue: ref('wb_sunny') };
  },
};
</script>

<style lang="scss">
#app {
  position: relative;
  display: flex;
}

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
