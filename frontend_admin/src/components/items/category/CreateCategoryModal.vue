<template>
  <div class="create-category-modal">
    <h2>Создание Категории</h2>

    <it-input
      v-model="form.name"
      :status="v$.name.$errors.length ? 'danger' : undefined"
      :message="
        v$.name.$errors.length ? v$.name.$errors[0].$message : undefined
      "
      label-top="* Имя"
      placeholder="Имя Категории"
    />

    <it-input
      v-model="form.title"
      :status="v$.title.$errors.length ? 'danger' : undefined"
      :message="
        v$.title.$errors.length ? v$.title.$errors[0].$message : undefined
      "
      label-top="* Заголовок"
      placeholder="Заголовок Категории"
    />

    <it-input v-model="form.parent" label-top="ID Родителя" placeholder="0" />

    <it-input v-model="form.slug" label-top="Slug" placeholder="my-category" />

    <it-button type="primary" @click="formSubmit">Создать Категорию</it-button>
  </div>
</template>

<script>
import useVuelidate from '@vuelidate/core';
import { required, helpers } from '@vuelidate/validators';
import { ref, computed, getCurrentInstance } from 'vue';
import { useStore } from 'vuex';

const requiredRus = helpers.withMessage('Это поле обязательно', required);

export default {
  props: {
    modelValue: { type: Boolean, default: false },
    parentId: { type: [String, Number], default: '0' },
  },
  emits: ['update:modelValue'],
  setup(props, { emit }) {
    const store = useStore();
    const app = getCurrentInstance();

    const showMessage = app.appContext.config.globalProperties.$Message;

    const form = ref({
      parent: Number(props.parentId),
      name: null,
      title: '',
      slug: '',
    });

    const rules = computed(() => ({
      name: { requiredRus },
      title: { requiredRus },
      parent: { requiredRus },
    }));
    const v$ = useVuelidate(rules, form);

    const formSubmit = async () => {
      const result = await v$.value.$validate();
      if (!result) {
        showMessage.warning({ text: 'Что-то пошло не так!' });
      } else {
        await store.dispatch('createCategory', {
          name: form.value.name,
          title: form.value.title,
          slug: form.value.slug,
          parent_id: form.value.parent,
        });
        if (form.value.parent) {
          await store.dispatch('fetchCategoryById', { id: form.value.parent });
        }
        setTimeout(() => {}, 500);
        emit('update:modelValue', false);

        form.value = {
          parent: Number(props.parentId),
          name: null,
          title: '',
          slug: '',
        };

        v$.value.$reset();
        showMessage.success({ text: 'Товар создан.' });
      }
    };

    return { v$, form, formSubmit };
  },
};
</script>

<style lang="scss" scoped>
.create-category-modal {
  & > * + * {
    margin-bottom: 15px;
  }
}
h2 {
  margin-bottom: 15px;
}
</style>
