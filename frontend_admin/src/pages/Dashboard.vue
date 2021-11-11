<template>
  <div class="dashboard">
    <h1 class="title">Админ Панель</h1>

    <div class="container">
      <div class="tiles">
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
import { ref } from 'vue';
import { useStore } from 'vuex';
import InfoTile from '../components/dashboard/InfoTile.vue';

export default {
  name: 'Home',
  components: { InfoTile },
  setup() {
    const store = useStore();
    const ordersCount = ref(251);
    const productsCount = ref(56);
    const categoriesCount = ref(8);
    return { ordersCount, productsCount, categoriesCount };
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

  .tiles {
    display: flex;

    & > *:not(:last-child) {
      margin-right: 28px;
    }
  }
}
</style>
