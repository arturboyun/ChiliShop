<template>
  <div class="table">
    <table>
      <tr>
        <th>ID</th>
        <th>ID Родителя</th>
        <th>Имя</th>
        <th>Заголовок</th>
        <th>Slug</th>
        <th>Подкатегорий</th>
        <th>Действия</th>
      </tr>
      <tr v-for="(category, index) in categories" :key="index">
        <td>{{ category.id }}</td>
        <td>{{ category.parent_id || 0 }}</td>
        <td>{{ category.name }}</td>
        <td>{{ category.title }}</td>
        <td>{{ category.slug }}</td>
        <td>{{ category.children.length }}</td>
        <td>
          <div class="actions">
            <it-button
              type="primary"
              icon="edit"
              @click="async () => await openEditModal(category)"
            />
            <it-button
              type="danger"
              icon="delete"
              @click="async () => await openDeleteModal(category)"
            />
            <router-link
              v-if="category.children.length > 0"
              :to="`/category/${category.slug}/`"
            >
              <it-button type="black" icon="visibility" />
            </router-link>
          </div>
        </td>
      </tr>
    </table>
  </div>

  <it-modal v-model="confirmDeleteModal">
    <template #body>
      <DeleteCategoryModal
        v-if="Object.keys(selectedCategory).length"
        v-model="confirmDeleteModal"
        :category="selectedCategory"
      />
    </template>
  </it-modal>

  <it-modal v-model="editCategoryModal">
    <template #body>
      <EditCategoryModal
        v-if="Object.keys(selectedCategory).length"
        v-model="editCategoryModal"
        :category="selectedCategory"
      />
    </template>
  </it-modal>
</template>

<script>
import { ref, watch } from 'vue';
import DeleteCategoryModal from '@/components/items/category/DeleteCategoryModal';
import EditCategoryModal from '@/components/items/category/EditCategoryModal';

export default {
  name: 'CategoriesTable',
  components: { EditCategoryModal, DeleteCategoryModal },
  props: { categories: { type: Array, required: true } },
  setup(props) {
    const confirmDeleteModal = ref(false);
    const editCategoryModal = ref(false);
    const selectedCategory = ref({});

    const openDeleteModal = async (category) => {
      selectedCategory.value = category;
      confirmDeleteModal.value = true;
    };

    const openEditModal = async (category) => {
      selectedCategory.value = category;
      editCategoryModal.value = true;
    };

    watch(confirmDeleteModal, (newValue) => {
      if (!newValue) selectedCategory.value = {};
    });

    watch(editCategoryModal, (newValue) => {
      if (!newValue) selectedCategory.value = {};
    });

    return {
      selectedCategory,
      editCategoryModal,
      confirmDeleteModal,
      openDeleteModal,
      openEditModal,
    };
  },
};
</script>
<style scoped lang="scss"></style>
