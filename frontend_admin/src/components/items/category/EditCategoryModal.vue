<template>
  <div class="edit-category-modal">
    <h2>Редактирование Категории</h2>

    <it-input
      v-model="form.name"
      :status="v$.name.$errors.length ? 'danger' : undefined"
      :message="
        v$.name.$errors.length ? v$.name.$errors[0].$message : undefined
      "
      label-top="Имя"
      placeholder="Имя Категории"
    />

    <it-input
      v-model="form.title"
      :status="v$.title.$errors.length ? 'danger' : undefined"
      :message="
        v$.title.$errors.length ? v$.title.$errors[0].$message : undefined
      "
      label-top="Заголовок"
      placeholder="Заголовок Категории"
    />

    <it-input
      v-model="form.parent_id"
      label-top="ID Родителя"
      placeholder="0"
    />

    <it-input v-model="form.slug" label-top="Slug" placeholder="my-category" />

    <it-button type="primary" @click="formSubmit">Изменить Категорию</it-button>
  </div>
</template>

<script>
import useVuelidate from '@vuelidate/core';
import { required, helpers } from '@vuelidate/validators';
import {
  ref,
  computed,
  getCurrentInstance,
  onMounted,
  reactive,
  watch,
} from 'vue';
import { useStore } from 'vuex';

const requiredRus = helpers.withMessage('Это поле обязательно', required);

export default {
  props: {
    modelValue: { type: Boolean, default: false },
    category: { type: Object, required: true },
  },
  emits: ['update:modelValue'],
  setup(props, { emit }) {
    const app = getCurrentInstance();
    const store = useStore();
    const showMessage = app.appContext.config.globalProperties.$Message;

    const form = reactive({
      name: props.category.name,
      title: props.category.title,
      slug: props.category.slug,
      parent_id: props.category.parent_id || 0,
    });

    const rules = computed(() => ({
      name: { requiredRus },
      title: { requiredRus },
      parent_id: { requiredRus },
    }));
    const v$ = useVuelidate(rules, form);

    const formSubmit = async () => {
      const result = await v$.value.$validate();
      if (!result) {
        console.log(v$.value.$errors);
        showMessage.warning({ text: 'Что-то пошло не так!' });
      } else {
        await store.dispatch('updateCategory', { id: props.category.id, form });
        if (props.category.parent_id) {
          await store.dispatch('fetchCategoryById', {
            id: props.category.parent_id,
          });
        }
        setTimeout(() => {}, 500);
        emit('update:modelValue', false);
      }
    };

    return { v$, form, formSubmit };
  },
};
</script>

<style lang="scss" scoped>
.edit-category-modal {
  & > * + * {
    margin-bottom: 15px;
  }
}
h2 {
  margin-bottom: 15px;
}
</style>
