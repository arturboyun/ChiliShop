<template>
  <div class="categories">
    <h1 class="title">Категории</h1>

    <div class="actions">
      <div class="col"></div>
      <div class="col">
        <it-button
          class="create-category-btn"
          type="primary"
          round
          @click="createCategoryModal = true"
        >
          Создать Категорию
        </it-button>
      </div>
    </div>

    <div v-if="loading" class="loading">
      <it-loading />
    </div>

    <CategoriesTable v-else-if="categories.length" :categories="categories" />

    <div v-else class="not-categories">Категорий не найдено.</div>

    <it-modal v-model="createCategoryModal">
      <template #body>
        <CreateCategoryModal v-model="createCategoryModal" />
      </template>
    </it-modal>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import CategoriesTable from '../components/items/CategoriesTable';
import CreateCategoryModal from '@/components/global/CreateCategoryModal';

export default {
  name: 'Categories',
  components: { CreateCategoryModal, CategoriesTable },
  setup() {
    const store = useStore();

    const loading = ref(true);
    const createCategoryModal = ref(false);

    const categories = computed(() => store.getters.getCategories);

    onMounted(async () => {
      loading.value = true;
      await store.dispatch('fetchCategories', { skip: 0, limit: 100 });
      setTimeout(() => (loading.value = false), 1200);
    });

    return { categories, loading, createCategoryModal };
  },
};
</script>

<style lang="scss" scoped>
.categories {
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

  .current-category-not-found {
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 900;
    font-size: 18px;
  }
}
</style>
