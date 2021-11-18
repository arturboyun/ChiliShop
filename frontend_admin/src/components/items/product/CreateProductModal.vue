<template>
  <div class="create-product-modal">
    <h2>Создание Товара</h2>

    <it-input
      v-model="form.title"
      :status="v$.title.$errors.length ? 'danger' : undefined"
      :message="
        v$.title.$errors.length ? v$.title.$errors[0].$message : undefined
      "
      label-top="* Название"
      placeholder="Название Товара"
    />

    <it-input v-model="form.slug" label-top="Slug" placeholder="product-slug" />

    <it-textarea
      v-model="form.description"
      label-top="Описание"
      placeholder="Описание Товара"
    />

    <div class="group">
      <it-input
        v-model.number="form.price"
        :status="v$.price.$errors.length ? 'danger' : undefined"
        :message="
          v$.price.$errors.length ? v$.price.$errors[0].$message : undefined
        "
        label-top="* Цена"
        placeholder="1000"
      />
      <it-input
        v-model="form.quantity"
        :status="v$.quantity.$errors.length ? 'danger' : undefined"
        :message="
          v$.quantity.$errors.length
            ? v$.quantity.$errors[0].$message
            : undefined
        "
        label-top="* Количество"
        placeholder="100"
      />
    </div>

    <it-input
      v-model.number="form.category_id"
      :status="v$.category_id.$errors.length ? 'danger' : undefined"
      :message="
        v$.category_id.$errors.length
          ? v$.category_id.$errors[0].$message
          : undefined
      "
      label-top="* ID Категории"
      placeholder="21"
    />

    <it-input
      v-model="form.top_sizes"
      label-top="Размеры Верх"
      placeholder="M, S, L, XL, XXL"
    />

    <it-input
      v-model="form.sizes"
      :status="v$.sizes.$errors.length ? 'danger' : undefined"
      :message="
        v$.sizes.$errors.length ? v$.sizes.$errors[0].$message : undefined
      "
      label-top="* Размеры"
      placeholder="M, S, L, XL, XXL"
    />

    <it-button type="primary" @click="formSubmit">Создать Товар</it-button>
  </div>
</template>

<script>
import { useStore } from 'vuex';
import { computed, getCurrentInstance, reactive, ref } from 'vue';
import useVuelidate from '@vuelidate/core';
import { helpers, required } from '@vuelidate/validators';

const requiredRus = helpers.withMessage('Это поле обязательно', required);

export default {
  name: 'CreateProductModal',
  props: {
    modelValue: { type: Boolean, default: false },
    categoryId: { type: [String, Number], default: null },
  },
  emits: ['update:modelValue'],
  setup(props, context) {
    const store = useStore();
    const app = getCurrentInstance();
    const showMessage = app.appContext.config.globalProperties.$Message;

    const form = reactive({
      title: '',
      slug: '',
      description: '',
      price: null,
      quantity: null,
      category_id: props.categoryId,
      top_sizes: '',
      sizes: '',
    });

    const rules = computed(() => ({
      title: { requiredRus },
      slug: {},
      description: {},
      price: { requiredRus },
      quantity: { requiredRus },
      category_id: { requiredRus },
      top_sizes: {},
      sizes: { requiredRus },
    }));
    const v$ = useVuelidate(rules, form);

    const formSubmit = async () => {
      const result = await v$.value.$validate();
      console.log(result);
      if (!result) {
        showMessage.warning({ text: 'Что-то пошло не так!' });
      } else {
        await store.dispatch('createProduct', form);
        setTimeout(() => {}, 500);
        context.emit('update:modelValue', false);
      }
    };

    return { v$, form, formSubmit };
  },
};
</script>

<style scoped lang="scss">
.create-product-modal {
  & > * + * {
    margin-bottom: 15px;
  }

  .group {
    display: flex;

    *:not(:last-child) {
      margin-right: 15px;
    }
  }
}

h2 {
  margin-bottom: 15px;
}
</style>
