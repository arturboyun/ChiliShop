<template>
  <div class="table">
    <table>
      <tr>
        <th>ID</th>
        <th>Категория</th>
        <th>Название</th>
        <th>Цена</th>
        <th>Количество</th>
        <th>Размеры Верх</th>
        <th>Размеры</th>
        <th>Действия</th>
      </tr>
      <tr v-for="(product, index) in products" :key="index">
        <td>{{ product.id }}</td>
        <td>{{ product.category_id }}</td>
        <td>{{ product.title }}</td>
        <td>{{ product.price }}</td>
        <td>{{ product.quantity }}</td>
        <td>
          <it-select placeholder="Просмотр" :options="product.top_sizes" />
        </td>
        <td>
          <it-select
            :placeholder="product.sizes.join(', ')"
            :options="product.sizes"
          />
        </td>
        <td>
          <div class="actions">
            <it-button
              type="primary"
              icon="edit"
              @click="() => openEditModal(product)"
            />
            <it-button
              type="danger"
              icon="delete"
              @click="() => openDeleteModal(product)"
            />
          </div>
        </td>
      </tr>
    </table>
  </div>

  <it-modal v-model="confirmDeleteModal">
    <template #body>
      <DeleteProductModal
        v-if="Object.keys(selectedProduct).length"
        v-model="confirmDeleteModal"
        :product="selectedProduct"
      />
    </template>
  </it-modal>

  <!--  <it-modal v-model="editCategoryModal">-->
  <!--    <template #body>-->
  <!--      <EditCategoryModal-->
  <!--        v-if="Object.keys(selectedCategory).length"-->
  <!--        v-model="editCategoryModal"-->
  <!--        :category="selectedCategory"-->
  <!--      />-->
  <!--    </template>-->
  <!--  </it-modal>-->
</template>

<script>
import { ref, watch } from 'vue';
import DeleteProductModal from '@/components/items/product/DeleteProductModal';

export default {
  name: 'ProductsTable',
  components: { DeleteProductModal },
  props: { products: { type: Array, required: true } },
  setup(props) {
    const confirmDeleteModal = ref(false);
    const selectedProduct = ref({});

    const openDeleteModal = async (category) => {
      selectedProduct.value = category;
      confirmDeleteModal.value = true;
    };

    // const openEditModal = async (category) => {
    //   selectedCategory.value = category;
    //   editCategoryModal.value = true;
    // };

    watch(confirmDeleteModal, (newValue) => {
      if (!newValue) selectedProduct.value = {};
    });

    // watch(editCategoryModal, (newValue) => {
    //   if (!newValue) selectedProduct.value = {};d
    // });

    return { confirmDeleteModal, selectedProduct, openDeleteModal };
  },
};
</script>

<style scoped></style>
