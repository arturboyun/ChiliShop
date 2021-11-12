<template>
  <div class="category">
    <h1 class="title">Категории</h1>

    <div class="actions">
      <div class="col">
        <h3 v-if="Object.keys(category).length > 0">
          Категория: {{ category.name }}
        </h3>
      </div>
      <div class="col">
        <it-button class="create-category-btn" type="primary" round>
          Создать Категорию
        </it-button>
      </div>
    </div>

    <div v-if="loading" class="loading">
      <it-loading />
    </div>

    <CategoriesTable
      v-else-if="!loading && Object.keys(category).length > 0"
      :categories="category.children"
    />
    <div v-else class="current-category-not-found">Категория не найдена</div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import CategoriesTable from '../components/items/CategoriesTable';

export default {
  name: 'Category',
  components: { CategoriesTable },
  setup() {
    const route = useRoute();
    const store = useStore();

    const loading = ref(true);

    const category = computed(() => store.getters.getCurrentCategory);

    onMounted(async () => {
      const slug = route.params.slug;
      loading.value = true;
      await store.dispatch('fetchCategoryBySlug', { slug });
      setTimeout(() => (loading.value = false), 1200);
    });

    return { category, loading };
  },
};
</script>

<style lang="scss" scoped>
.category {
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
