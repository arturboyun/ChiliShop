<template>
  <div class="dashboard">
    <h1 class="title">Админ Панель</h1>

    <div class="container">
      <div v-if="loading" class="loading">
        <it-loading />
      </div>
      <div v-else class="tiles">
        <info-tile
          icon-name="shopping_basket"
          title="Заказы"
          color="#6fbe60"
          :numbers="ordersCount"
        />
        <info-tile
          icon-name="local_offer"
          title="Товары"
          color="#c94e4e"
          :numbers="productsCount"
        />
        <info-tile
          icon-name="sort"
          title="Категории"
          color="#c9984e"
          :numbers="categoriesCount"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { computed, onMounted, ref } from 'vue';
import { useStore } from 'vuex';
import InfoTile from '../components/dashboard/InfoTile.vue';

export default {
  name: 'Home',
  components: { InfoTile },
  setup() {
    const store = useStore();
    const loading = ref(false);

    const ordersCount = ref(0);
    const productsCount = ref(0);
    const categoriesCount = computed(() => store.getters.getCategoriesCount);

    onMounted(async () => {
      loading.value = true;
      await store.dispatch('fetchCategories', { skip: 0, limit: 999 });
      setTimeout(() => (loading.value = false), 1200);
    });

    return { loading, ordersCount, productsCount, categoriesCount };
  },
};
</script>

<style lang="scss" scoped>
.dashboard {
  .title {
    margin-bottom: 28px;
  }

  .container {
    display: flex;
  }

  .loading {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .tiles {
    display: flex;

    & > *:not(:last-child) {
      margin-right: 28px;
    }
  }
}
</style>
