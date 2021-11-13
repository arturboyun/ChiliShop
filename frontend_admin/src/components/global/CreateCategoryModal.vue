<template>
  <div class="category-modal">
    <h2>Создание Категории</h2>
    <it-input
      v-model="form.name"
      :status="v$.name.$errors.length ? 'danger' : ''"
      :message="v$.name.$errors.length && v$.name.$errors[0].$message"
      label-top="* Имя"
      placeholder="Имя Категории"
    />
    <it-input
      v-model="form.title"
      :status="v$.title.$errors.length ? 'danger' : ''"
      :message="v$.title.$errors.length && v$.title.$errors[0].$message"
      label-top="* Заголовок"
      placeholder="Заголовок Категории"
    />
    <it-input v-model="form.parent" label-top="ID Родителя" placeholder="0" />
    <it-input v-model="form.slug" label-top="Slug" placeholder="my-category" />
    <it-button @click="submit" type="primary">Создать Категорию</it-button>
  </div>
</template>

<script>
import useVuelidate from '@vuelidate/core';
import { required, numeric, helpers } from '@vuelidate/validators';
import { ref, computed } from 'vue';

const requiredRus = helpers.withMessage('Это поле обязательно', required);

export default {
  props: {
    parentId: { type: [String || Number], default: 0 },
  },
  setup(props) {
    const form = ref({
      parent: ref(Number(props.parentId)),
      name: ref(null),
      title: ref(''),
      slug: ref(''),
    });

    const rules = computed(() => ({
      name: { requiredRus },
      title: { requiredRus },
      parent: { requiredRus, numeric },
    }));
    const v$ = useVuelidate(rules, form);

    const formSubmit = async () => {
      const result = await v$.value.$validate();
      console.log(result);
      if (!result) {
        // notify user form is invalid
        return;
      }
      // perform async actions
    };

    return { v$, form, submit: formSubmit };
  },
};
</script>

<style lang="scss" scoped>
.category-modal {
  & > * + * {
    margin-bottom: 15px;
  }
}
h2 {
  margin-bottom: 15px;
}
</style>
