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
            <it-button type="primary" icon="edit" />
            <it-button
              type="danger"
              icon="delete"
              @click="openDeleteModal(category)"
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
</template>

<script>
import { ref } from 'vue';
import DeleteCategoryModal from '@/components/global/DeleteCategoryModal';

export default {
  name: 'CategoriesTable',
  components: { DeleteCategoryModal },
  props: { categories: { type: Array, required: true } },
  setup(props) {
    const confirmDeleteModal = ref(false);
    const selectedCategory = ref({});

    const openDeleteModal = (category) => {
      selectedCategory.value = category;
      confirmDeleteModal.value = true;
    };

    return { props, openDeleteModal, selectedCategory, confirmDeleteModal };
  },
};
</script>
<style scoped lang="scss"></style>
