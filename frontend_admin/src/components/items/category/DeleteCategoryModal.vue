<template>
  <div class="delete-category-modal">
    <h3>Удаление Категории</h3>
    <p class="text">
      Вы уверены, что желаете удалить категорию <b>"{{ category.name }}"</b> и
      <b>ID {{ category.id }}</b> ?
    </p>
    <div class="actions">
      <it-button @click="close">Cancel</it-button>
      <it-button type="danger" @click="deleteCategory">Delete</it-button>
    </div>
  </div>
</template>

<script>
import { getCurrentInstance, ref, watch } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'DeleteCategoryModal',
  props: {
    modelValue: { type: Boolean, default: false },
    category: { type: Object, required: true },
  },
  emits: ['update:modelValue'],
  setup(props, { emit }) {
    const app = getCurrentInstance();
    const store = useStore();

    const showMessage = app.appContext.config.globalProperties.$Message;

    const close = () => {
      emit('update:modelValue', false);
    };
    const deleteCategory = async () => {
      await store.dispatch('deleteCategory', { categoryId: props.category.id });
      if (props.category.parent_id) {
        await store.dispatch('fetchCategoryById', {
          id: props.category.parent_id,
        });
      }
      setTimeout(() => {
        showMessage.success({ text: 'Категория удалена' });
        close();
      }, 200);
    };
    return { close, deleteCategory };
  },
};
</script>

<style scoped lang="scss">
h3 {
  margin-bottom: 15px;
}

.text {
  margin-bottom: 15px;
}

.actions {
  display: flex;
  align-items: center;
  justify-content: flex-end;

  *:not(:last-child) {
    margin-right: 15px;
  }
}
</style>
