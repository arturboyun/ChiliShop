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
        <div class="row">
          <it-button
            class="create-category-btn"
            type="primary"
            round
            @click="createCategoryModal = true"
          >
            Создать Категорию
          </it-button>
          <it-button
            class="create-product-btn"
            type="primary"
            round
            @click="createProductModalIsOpen = true"
          >
            Создать Товар
          </it-button>
        </div>
      </div>
    </div>

    <div v-if="loading" class="loading">
      <it-loading />
    </div>

    <CategoriesTable
      v-else-if="
        !loading &&
        Object.keys(category).length > 0 &&
        category.children.length > 0
      "
      :categories="category.children"
    />
    <div
      v-else-if="category.children.length <= 0"
      class="current-category-not-found"
    >
      Подкатегорий не найдено.
    </div>
    <div v-else class="current-category-not-found">Категория не найдена</div>

    <it-modal v-model="createCategoryModal">
      <template #body>
        <CreateCategoryModal
          v-model="createCategoryModal"
          :parent-id="category.id"
        />
      </template>
    </it-modal>

    <it-modal v-model="createProductModalIsOpen">
      <template #body>
        <CreateProductModal
          v-if="createProductModalIsOpen"
          v-model="createProductModalIsOpen"
          :category-id="category.id"
        />
      </template>
    </it-modal>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import CategoriesTable from '../components/items/category/CategoriesTable';
import CreateCategoryModal from '../components/items/category/CreateCategoryModal';
import CreateProductModal from '@/components/items/product/CreateProductModal';

export default {
  name: 'Category',
  components: { CreateProductModal, CategoriesTable, CreateCategoryModal },
  setup() {
    const route = useRoute();
    const store = useStore();

    const loading = ref(true);
    const createCategoryModal = ref(false);
    const createProductModalIsOpen = ref(false);

    const category = computed(() => store.getters.getCurrentCategory);

    const fetchCategories = async (slug) => {
      loading.value = true;
      await store.dispatch('fetchCategoryBySlug', { slug });
      setTimeout(() => (loading.value = false), 500);
    };

    onMounted(async () => {
      await fetchCategories(route.params.slug);
    });

    watch(
      () => route.params.slug,
      async (newValue) => {
        if (newValue) await fetchCategories(newValue);
      }
    );

    return { category, loading, createCategoryModal, createProductModalIsOpen };
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

    .col {
      display: flex;
      flex-direction: column;

      .row {
        display: flex;

        *:not(:last-child) {
          margin-right: 15px;
        }
      }
    }
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
