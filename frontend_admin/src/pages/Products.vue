<template>
  <div class="products">
    <h1 class="title">Товары</h1>

    <div class="actions">
      <div class="col"></div>
      <div class="col">
        <it-button
          class="create-category-btn"
          type="primary"
          round
          @click="createProductModalIsOpen = true"
        >
          Создать Товар
        </it-button>
      </div>
    </div>

    <div v-if="loading" class="loading">
      <it-loading />
    </div>

    <ProductsTable v-else-if="products.length" :products="products" />
    <div v-else class="no-products">Товаров не найдено.</div>

    <it-modal v-model="createProductModalIsOpen">
      <template #body>
        <CreateProductModal
          v-if="createProductModalIsOpen"
          v-model="createProductModalIsOpen"
        />
      </template>
    </it-modal>
  </div>
</template>
<script>
import ProductsTable from '@/components/items/product/ProductsTable';
import { computed, onMounted, ref } from 'vue';
import { useStore } from 'vuex';
import CreateProductModal from '@/components/items/product/CreateProductModal';
export default {
  components: { CreateProductModal, ProductsTable },
  setup() {
    const store = useStore();
    const loading = ref(true);
    const products = computed(() => store.getters.getProducts);
    const createProductModalIsOpen = ref(false);

    onMounted(async () => {
      loading.value = true;
      await store.dispatch('fetchProducts', { skip: 0, limit: 100 });
      setTimeout(() => (loading.value = false), 500);
    });

    return { products, loading, createProductModalIsOpen };
  },
};
</script>

<style lang="scss" scoped>
.products {
  width: 100%;

  .title {
    margin-bottom: 25px;
  }

  .loading {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .actions {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 15px;
  }

  .no-products {
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 900;
    font-size: 18px;
  }
}
</style>
