<template>
  <div class="delete-product-modal">
    <h3>Удаление Товара</h3>
    <p class="text">
      Вы уверены, что желаете удалить товар <b>"{{ product.title }}"</b> и
      <b>ID {{ product.id }}</b> ?
    </p>
    <div class="actions">
      <it-button @click="close">Отмена</it-button>
      <it-button type="danger" @click="deleteProduct">Удалить</it-button>
    </div>
  </div>
</template>

<script>
import { getCurrentInstance } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'DeleteProductModal',
  props: {
    modelValue: { type: Boolean, default: false },
    product: { type: Object, required: true },
  },
  emits: ['update:modelValue'],
  setup(props, { emit }) {
    const app = getCurrentInstance();
    const store = useStore();

    const showMessage = app.appContext.config.globalProperties.$Message;

    const close = () => {
      emit('update:modelValue', false);
    };

    const deleteProduct = async () => {
      await store.dispatch('deleteProduct', { id: props.product.id });

      setTimeout(() => {
        showMessage.success({ text: 'Товар удален.' });
        close();
      }, 500);
    };
    return { close, deleteProduct };
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
